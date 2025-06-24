from fastapi import APIRouter, Request
import os
import requests

router = APIRouter()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

@router.post("/")
async def create_deposit(req: Request):
    body = await req.json()
    res = requests.post(
        f"{SUPABASE_URL}/rest/v1/deposits",
        headers={
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
            "Prefer": "return=representation"
        },
        json={
            "game_id": body['game_id'],
            "amount": body['amount'],
            "slip_url": body['slip_url']
        }
    )
    return res.json()
