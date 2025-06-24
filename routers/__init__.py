# routers/__init__.py - Proper router exports

from .user_router import router as user_router
from .deposit_router import router as deposit_router
from .withdraw_router import router as withdraw_router
from .broadcast_router import router as broadcast_router  # Rename brocast_router.py → broadcast_router.py
from .phone_router import router as phone_router
from .upload_router import router as upload_router

__all__ = [
    "user_router",
    "deposit_router", 
    "withdraw_router",
    "broadcast_router",
    "phone_router",
    "upload_router"
]
