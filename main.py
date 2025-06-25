from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# ✅ Router imports
from routers import (
    user_router,
    deposit_router,
    withdraw_router,
    broadcast_router,
    phone_router,
    upload_router,
    viber_bot_router,          # ✅ Viber Bot Control API
    viber_user_register_router # ✅ Viber User Account Opening
)

# ✅ Initialize app
app = FastAPI()

# ✅ CORS middleware config (allow frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your dashboard domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Static files and templates setup
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# ✅ Core Functional Routers
app.include_router(user_router, prefix="/api/v1/user", tags=["User Management"])
app.include_router(deposit_router, prefix="/api/v1/deposit", tags=["Deposit"])
app.include_router(withdraw_router, prefix="/api/v1/withdraw", tags=["Withdraw"])
app.include_router(broadcast_router, prefix="/api/v1/broadcast", tags=["Broadcast"])
app.include_router(phone_router, prefix="/api/v1/phone", tags=["Phone Management"])
app.include_router(upload_router, prefix="/api/v1/slip", tags=["Upload Management"])

# ✅ Viber Bot API Routers
app.include_router(viber_bot_router, prefix="/api/v1/bot", tags=["Viber Bot Control"])
app.include_router(viber_user_register_router, prefix="/api/v1/viber", tags=["Viber User Register"])

# ✅ UI Home (Matrix style default page)
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
