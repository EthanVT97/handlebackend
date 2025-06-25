# routers/slip_router.py (Fixed)

from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from sqlalchemy.orm import Session
from auth.oauth2 import get_current_user
from models import models
import shutil
import uuid
import os
from pathlib import Path

router = APIRouter()

# FIX: Define allowed file types and max size to prevent RCE and DoS.
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".pdf"}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB
UPLOAD_DIRECTORY = "uploads"

# Ensure the upload directory exists
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

@router.post("/uploadslip/")
async def upload_slip(
    file: UploadFile = File(...),
    current_user: models.User = Depends(get_current_user)
):
    # FIX (File Size): Check the file size to prevent Denial of Service.
    # We check the size by seeking to the end of the file stream.
    file.file.seek(0, 2)
    file_size = file.file.tell()
    file.file.seek(0) # Reset file pointer
    if file_size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"File size exceeds the limit of {MAX_FILE_SIZE / 1024 / 1024} MB."
        )

    # FIX (File Type): Validate the file extension against a whitelist.
    file_extension = Path(file.filename).suffix.lower()
    if file_extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid file type. Allowed types are: {', '.join(ALLOWED_EXTENSIONS)}"
        )

    # FIX (Path Traversal): Generate a new, secure filename using UUID.
    # This completely prevents the user from controlling the path or filename on the server.
    safe_filename = f"{uuid.uuid4()}{file_extension}"
    file_path = os.path.join(UPLOAD_DIRECTORY, safe_filename)

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Could not save file: {e}"
        )
    finally:
        await file.close()

    return {
        "message": f"Slip for user '{current_user.username}' uploaded successfully.",
        "filename": safe_filename
    }
