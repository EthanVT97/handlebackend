# routers/viber_bot_router.py

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional
import datetime

router = APIRouter()

# Mock state (replace with DB or Supabase later)
BOT_STATUS = {"enabled": True}
WELCOME_MESSAGE = {"text": "👋 Welcome to ShweChat Viber Bot!"}
AUTO_REPLIES = []
WEBHOOK_URL = {"url": ""}
BOT_LOGS = []

# ✅ Models
class BotStatus(BaseModel):
    enabled: bool

class WelcomeMessage(BaseModel):
    text: str

class AutoReply(BaseModel):
    keyword: str
    response: str

class WebhookPayload(BaseModel):
    url: str

class SimulateMessage(BaseModel):
    sender: str
    message: str

# ✅ Endpoints
@router.get("/status")
def get_status():
    return BOT_STATUS

@router.post("/status")
def set_status(payload: BotStatus):
    BOT_STATUS["enabled"] = payload.enabled
    return {"message": "Bot status updated", "enabled": BOT_STATUS["enabled"]}

@router.get("/welcome")
def get_welcome():
    return WELCOME_MESSAGE

@router.post("/welcome")
def set_welcome(payload: WelcomeMessage):
    WELCOME_MESSAGE["text"] = payload.text
    return {"message": "Welcome message updated", "text": WELCOME_MESSAGE["text"]}

@router.get("/auto-reply")
def list_auto_replies():
    return {"rules": AUTO_REPLIES}

@router.post("/auto-reply")
def add_auto_reply(payload: AutoReply):
    AUTO_REPLIES.append({
        "keyword": payload.keyword.lower(),
        "response": payload.response
    })
    return {"message": "Auto reply added", "rules": AUTO_REPLIES}

@router.post("/webhook")
def set_webhook(payload: WebhookPayload):
    WEBHOOK_URL["url"] = payload.url
    return {"message": "Webhook URL updated", "url": WEBHOOK_URL["url"]}

@router.get("/logs")
def get_logs():
    return {"logs": BOT_LOGS}

@router.post("/simulate")
def simulate_msg(payload: SimulateMessage):
    log = {
        "sender": payload.sender,
        "message": payload.message,
        "time": str(datetime.datetime.now())
    }
    BOT_LOGS.append(log)

    auto_response = next((r["response"] for r in AUTO_REPLIES if r["keyword"] in payload.message.lower()), None)
    
    return {
        "log": log,
        "bot_enabled": BOT_STATUS["enabled"],
        "auto_reply": auto_response
    }
