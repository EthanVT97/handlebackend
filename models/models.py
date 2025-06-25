# models/models.py (Fixed)

from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, func, Numeric
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database.database import Base
from datetime import datetime
from decimal import Decimal

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)
    full_name: Mapped[str] = mapped_column(String, nullable=True)
    role: Mapped[str] = mapped_column(String, default="user")
    
    # FIX: Use Numeric(precision, scale) for currency to avoid float inaccuracies.
    # Storing up to 99,999,999.99
    balance: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=Decimal("0.00"))
    
    transactions: Mapped[list["Transaction"]] = relationship("Transaction", back_populates="user")

class Transaction(Base):
    __tablename__ = "transactions"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    
    # FIX: Also use Numeric here for consistency.
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    
    type: Mapped[str] = mapped_column(String) # "deposit" or "withdrawal"
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    
    user: Mapped["User"] = relationship("User", back_populates="transactions")
