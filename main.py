# main.py (Fixed)

from fastapi import FastAPI
from routers import user_router, deposit_router, withdraw_router, slip_router, viber_bot_router
from database.database import engine
from models import models
from fastapi_slowapi import Limiter, _rate_limit_exceeded_handler
from fastapi_slowapi.util import get_remote_address
from starlette.requests import Request

# Add the rate limiter instance
limiter = Limiter(key_func=get_remote_address)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Add state and exception handler for the limiter
app.state.limiter = limiter
app.add_exception_handler(_rate_limit_exceeded_handler)

app.include_router(user_router.router, prefix="/api/v1/users", tags=["users"])
app.include_router(deposit_router.router, prefix="/api/v1/deposits", tags=["deposits"])
app.include_router(withdraw_router.router, prefix="/api/v1/withdrawals", tags=["withdrawals"])
app.include_router(slip_router.router, prefix="/api/v1/slips", tags=["slips"])
app.include_router(viber_bot_router.router, prefix="/api/v1/viber", tags=["viber"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Handle Backend API"}
