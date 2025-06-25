# routers/__init__.py - All router exports

from .user_router import router as user_router
from .deposit_router import router as deposit_router
from .withdraw_router import router as withdraw_router
from .broadcast_router import router as broadcast_router  # ✅ Ensure file is named correctly
from .phone_router import router as phone_router
from .upload_router import router as slip_router

# ✅ Newly added Viber-related routers
from .viber_bot_router import router as viber_bot_router
from .viber_user_register_router import router as viber_user_register_router

__all__ = [
    "user_router",
    "deposit_router",
    "withdraw_router",
    "broadcast_router",
    "phone_router",
    "slip_router",
    "viber_bot_router",
    "viber_user_register_router"
]
