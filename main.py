from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import user_router, deposit_router, withdraw_router, broadcast_router, phone_router, upload_router

app = FastAPI()

# ✅ CORS Config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to frontend domain in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include all routers with prefixes
app.include_router(user_router, prefix="/api/v1/user", tags=["User Management"])
app.include_router(deposit_router, prefix="/api/v1/deposit", tags=["Deposit"])
app.include_router(withdraw_router, prefix="/api/v1/withdraw", tags=["Withdraw"])
app.include_router(broadcast_router, prefix="/api/v1/broadcast", tags=["Broadcast"])
app.include_router(phone_router, prefix="/api/v1/phone", tags=["Update Phone"])
app.include_router(upload_router, prefix="/api/v1/slip", tags=["Upload Slip"])

# ✅ Root Health Check
@app.get("/")
def root():
    return {"status": "Hello , Go away✅"}
