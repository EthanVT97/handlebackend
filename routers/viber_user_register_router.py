# routers/viber_user_register_router.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import uuid

router = APIRouter()

# Simulated in-memory user DB (replace with actual DB/Supabase)
viber_users = {}

# ✅ Model
class ViberUserRegister(BaseModel):
    sender_id: str   # unique Viber user ID
    name: Optional[str]
    phone: Optional[str]

@router.post("/register")
def register_user(user: ViberUserRegister):
    if user.sender_id in viber_users:
        return {"message": "User already registered", "user": viber_users[user.sender_id]}

    viber_users[user.sender_id] = {
        "id": str(uuid.uuid4()),
        "name": user.name or "Unnamed",
        "phone": user.phone or "Unknown",
        "joined": str(datetime.datetime.now())
    }

    return {
        "message": "User registered successfully",
        "user": viber_users[user.sender_id]
    }

@router.get("/user/{sender_id}")
def get_registered_user(sender_id: str):
    if sender_id not in viber_users:
        raise HTTPException(status_code=404, detail="User not found")
    return viber_users[sender_id]
