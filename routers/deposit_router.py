# routers/deposit_router.py (Fixed)

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import schemas
from models import models
from database import database
from auth.oauth2 import get_current_user
from decimal import Decimal

router = APIRouter()

@router.post("/", response_model=schemas.Transaction)
def create_deposit(
    transaction: schemas.TransactionCreate,
    db: Session = Depends(database.get_db),
    # FIX (IDOR): The user performing the action is identified by their token, not a URL parameter.
    current_user: models.User = Depends(get_current_user)
):
    # FIX: Amount validation is now handled in the Pydantic schema (schemas.py)
    # but an explicit check here is still good for defense-in-depth.
    if transaction.amount <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Deposit amount must be positive.")

    try:
        # FIX (Atomicity): All database changes are now within one transaction block.
        # This ensures that if any step fails, all previous steps are rolled back.
        
        # We operate on 'current_user' which was safely retrieved via the JWT token.
        # This completely resolves the IDOR vulnerability.
        current_user.balance += transaction.amount

        new_transaction = models.Transaction(
            user_id=current_user.id,
            amount=transaction.amount,
            type="deposit"
        )

        db.add(new_transaction)
        db.commit()
        db.refresh(new_transaction)
        
        return new_transaction
    
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred during the deposit process: {e}"
        )
