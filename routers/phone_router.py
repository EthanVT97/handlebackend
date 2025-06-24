# routers/phone_router.py

from fastapi import APIRouter, Request
import os
import requests

router = APIRouter()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

@router.put("/{game_id}")
async def update_user_phone(game_id: str, req: Request):
    try:
        data = await req.json()
        phone = data.get("phone")

        response = requests.patch(
            f"{SUPABASE_URL}/rest/v1/users?game_id=eq.{game_id}",
            headers={
                "apikey": SUPABASE_KEY,
                "Authorization": f"Bearer {SUPABASE_KEY}",
                "Content-Type": "application/json",
                "Prefer": "return=representation"
            },
            json={"phone": phone}
        )
        return response.json()
    except Exception as e:
        return {"error": str(e)}
