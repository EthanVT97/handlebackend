# routers/upload_router.py

from fastapi import APIRouter, UploadFile, File
import os
import uuid
import requests

router = APIRouter()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_BUCKET = "slips"  # Default bucket name

@router.post("/")
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
            return {"url": public_url}
        else:
            return {"error": res.text}

    except Exception as e:
        return {"error": str(e)}
