# routers/withdraw_router.py (Fixed)

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import schemas
from models import models
from database import database
from auth.oauth2 import get_current_user
from decimal import Decimal

router = APIRouter()

@router.post("/", response_model=schemas.Transaction)
def create_withdrawal(
    transaction: schemas.TransactionCreate,
    db: Session = Depends(database.get_db),
    # FIX (IDOR): Use the authenticated user from the token, not a user_id from the URL.
    current_user: models.User = Depends(get_current_user)
):
    # FIX: Amount validation to prevent negative withdrawals.
    if transaction.amount <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Withdrawal amount must be positive.")

    # FIX (Atomicity): Wrap the entire logic in a try/except block with rollback.
    try:
        # The 'current_user' object is locked to the authenticated user, fixing the IDOR flaw.
        if current_user.balance < transaction.amount:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Insufficient funds.")

        current_user.balance -= transaction.amount

        new_transaction = models.Transaction(
            user_id=current_user.id,
            amount=transaction.amount,
            type="withdrawal"
        )

        db.add(new_transaction)
        db.commit()
        db.refresh(new_transaction)

        return new_transaction
    
    except Exception as e:
        db.rollback()
        # Avoid re-raising the same HTTPException, which would bypass the 500 error handler.
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred during the withdrawal process: {e}"
        )
