import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Router imports
from routers import (
    user_router,
    deposit_router,
    withdraw_router,
    broadcast_router,
    phone_router,
    upload_router,
    viber_bot_router,
    viber_user_register_router,
)

app = FastAPI()

# CORS origins from env or default to localhost
origins = os.getenv("CORS_ORIGINS", "http://localhost,http://127.0.0.1").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Use env var for production safety
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files and template config
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Register routers
app.include_router(user_router, prefix="/api/v1/user", tags=["User Management"])
app.include_router(deposit_router, prefix="/api/v1/deposit", tags=["Deposit"])
app.include_router(withdraw_router, prefix="/api/v1/withdraw", tags=["Withdraw"])
app.include_router(broadcast_router, prefix="/api/v1/broadcast", tags=["Broadcast"])
app.include_router(phone_router, prefix="/api/v1/phone", tags=["Phone Management"])
app.include_router(upload_router, prefix="/api/v1/slip", tags=["Upload Management"])

app.include_router(viber_bot_router, prefix="/api/v1/bot", tags=["Viber Bot Control"])
app.include_router(viber_user_register_router, prefix="/api/v1/viber", tags=["Viber User Register"])

# Root route with template rendering
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
