from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

@app.post("/deposit")
async def create_deposit(req: Request):
    body = await req.json()
    game_id = body['game_id']
    amount = body['amount']
    slip_url = body['slip_url']

    res = requests.post(
        f"{SUPABASE_URL}/rest/v1/deposits",
        headers={
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
            "Prefer": "return=representation"
        },
        json={
            "game_id": game_id,
            "amount": amount,
            "slip_url": slip_url
        }
    )

    return res.json()
