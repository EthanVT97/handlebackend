from fastapi import APIRouter, Request
import os, requests

router = APIRouter()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

@router.post("/")
async def create_withdraw(req: Request):
    body = await req.json()
    res = requests.post(
        f"{SUPABASE_URL}/rest/v1/withdrawals",
        headers={
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
            "Prefer": "return=representation"
        },
        json={
            "game_id": body['game_id'],
            "amount": body['amount']
        }
    )
    return res.json()
