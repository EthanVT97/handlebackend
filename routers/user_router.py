# routers/user_router.py

from fastapi import APIRouter, Request
import os
import requests

router = APIRouter()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

@router.get("/")
async def get_all_users():
    res = requests.get(
        f"{SUPABASE_URL}/rest/v1/users",
        headers={
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json"
        }
    )
    return res.json()

@router.post("/")
async def create_user(req: Request):
    data = await req.json()
    res = requests.post(
        f"{SUPABASE_URL}/rest/v1/users",
        headers={
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
            "Prefer": "return=representation"
        },
        json=data
    )
    return res.json()
