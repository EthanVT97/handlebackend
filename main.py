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
    upload_router
)

app = FastAPI()

# ✅ CORS middleware config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Mount static files (for /static/matrix.css)
app.mount("/static", StaticFiles(directory="static"), name="static")

# ✅ Template directory setup
templates = Jinja2Templates(directory="templates")

# ✅ Router registration
app.include_router(user_router, prefix="/api/v1/user", tags=["User Management"])
app.include_router(deposit_router, prefix="/api/v1/deposit", tags=["Deposit"])
app.include_router(withdraw_router, prefix="/api/v1/withdraw", tags=["Withdraw"])
app.include_router(broadcast_router, prefix="/api/v1/broadcast", tags=["Broadcast"])
app.include_router(phone_router, prefix="/api/v1/phone", tags=["Update Phone"])
app.include_router(upload_router, prefix="/api/v1/slip", tags=["Upload Slip"])

# ✅ Root route with Matrix-style UI
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
