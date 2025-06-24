from fastapi import FastAPI, Request, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
import uuid

app = FastAPI()

# ✅ CORS Middleware (for frontend calls)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Frontend URL only in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Env Setup
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
CHATBOT_TOKEN = os.getenv("CHATBOT_TOKEN")
SUPABASE_BUCKET = "slips"  # default bucket name

### ✅ Health Check ###
@app.get("/")
def root():
    return { "status": "Viber Bot API Running ✅" }

### ✅ Deposit API ###
@app.post("/deposit")
async def create_deposit(req: Request):
    try:
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
    except Exception as e:
        return { "error": str(e) }

### ✅ Withdraw API ###
@app.post("/withdraw")
async def create_withdraw(req: Request):
    try:
        body = await req.json()
        game_id = body['game_id']
        amount = body['amount']

        res = requests.post(
            f"{SUPABASE_URL}/rest/v1/withdrawals",
            headers={
                "apikey": SUPABASE_KEY,
                "Authorization": f"Bearer {SUPABASE_KEY}",
                "Content-Type": "application/json",
                "Prefer": "return=representation"
            },
            json={
                "game_id": game_id,
                "amount": amount
            }
        )
        return res.json()
    except Exception as e:
        return { "error": str(e) }

### ✅ Broadcast to Chatrace Bot ###
@app.post("/broadcast")
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
                    "recipient": { "user_id": user_id },
                    "message": { "type": "text", "text": message }
                }
            )
            responses.append(res.json())
        return { "status": "done", "sent": len(responses) }
    except Exception as e:
        return { "error": str(e) }

### ✅ Update User Phone ###
@app.put("/users/{game_id}")
async def update_user(game_id: str, req: Request):
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
            json={ "phone": phone }
        )
        return response.json()
    except Exception as e:
        return { "error": str(e) }

### ✅ Get All Users ###
@app.get("/users")
async def get_users():
    response = requests.get(
        f"{SUPABASE_URL}/rest/v1/users",
        headers={
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json"
        }
    )
    return response.json()

### ✅ Upload Slip to Supabase Storage ###
@app.post("/upload-slip")
async def upload_slip(file: UploadFile = File(...)):
    try:
        file_bytes = await file.read()
        ext = file.filename.split('.')[-1]
        filename = f"{uuid.uuid4()}.{ext}"

        upload_url = f"{SUPABASE_URL}/storage/v1/object/{SUPABASE_BUCKET}/{filename}"

        headers = {
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": file.content_type,
            "x-upsert": "true"
        }

        res = requests.put(upload_url, headers=headers, data=file_bytes)

        if res.status_code == 200:
            public_url = f"{SUPABASE_URL}/storage/v1/object/public/{SUPABASE_BUCKET}/{filename}"
            return { "url": public_url }
        else:
            return { "error": res.text }

    except Exception as e:
        return { "error": str(e) }
