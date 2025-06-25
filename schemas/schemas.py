# schemas/schemas.py (Fixed)

from pydantic import BaseModel, EmailStr
from datetime import datetime
from decimal import Decimal # FIX: Import Decimal

# --- Transaction Schemas ---
class TransactionBase(BaseModel):
    # FIX: Use Decimal for financial amounts.
    amount: Decimal

    # FIX: Add validation to ensure amount is positive.
    class Config:
        orm_mode = True
        
    @validator('amount')
    def amount_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError('Amount must be positive')
        return value

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int
    user_id: int
    type: str
    timestamp: datetime

# --- User Schemas ---
class UserBase(BaseModel):
    username: str
    full_name: str | None = None

class UserCreate(UserBase):
    password: str
    # FIX: Remove role from create schema to prevent privilege escalation.
    # The role will be set on the server side.
    # role: str 

class User(UserBase):
    id: int
    role: str
    # FIX: Use Decimal for balance in response models.
    balance: Decimal
    transactions: list[Transaction] = []

    class Config:
        orm_mode = True
        
# --- Token Schemas ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None
