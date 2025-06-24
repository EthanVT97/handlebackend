# routers/broadcast_router.py

from fastapi import APIRouter, Request
import os
import requests

router = APIRouter()

CHATBOT_TOKEN = os.getenv("CHATBOT_TOKEN")

@router.post("/")
async def send_promo(req: Request):
    try:
        data = await req.json()
        message = data['message']
        users = data['users']

        responses = []
        for user_id in users:
            res = requests.post(
                "https://api.chatrace.com/api/v1/messages/send",
                headers={
                    "Authorization": f"Bearer {CHATBOT_TOKEN}",
                    "Content-Type": "application/json"
                },
                json={
                    "recipient": {"user_id": user_id},
                    "message": {"type": "text", "text": message}
                }
            )
            responses.append(res.json())

        return {"status": "done", "sent": len(responses)}
    except Exception as e:
        return {"error": str(e)}
