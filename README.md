🎮 Bot Backend API - Viber + Supabase + Chatrace Integration

This repository powers a lightweight FastAPI backend that handles deposit/withdrawal processing, slip uploads, promo broadcasting, and user phone management — designed for online game bot systems integrated with Viber and Chatrace.


---

🚀 Features

✅ Deposit & Withdrawal APIs

✅ Upload payment slips to Supabase Storage

✅ Broadcast promotional messages to Chatrace bot users

✅ User phone number management via Admin Panel

✅ Built with FastAPI and RESTful principles

✅ Easy deployment on Render platform


---

🧱 Tech Stack

Component	Description

FastAPI	Modern, fast Python web framework
Supabase	PostgreSQL database, Auth, Storage
Chatrace	Messaging Bot Broadcast System
Render	Cloud hosting with GitHub auto-deploy


---

📁 API Endpoints

Endpoint	Method	Description

/	GET	Health check / Dashboard homepage
/api/v1/deposit	POST	Submit deposit with slip image
/api/v1/withdraw	POST	Submit withdrawal request
/api/v1/broadcast	POST	Send promo message to bot users
/api/v1/user	GET	List all users
/api/v1/user/{id}	PUT	Update user phone number
/api/v1/slip	POST	Upload slip image to Supabase Storage


---

⚙️ Environment Variables (.env)

Create .env or .env.example in project root:

SUPABASE_URL=https://your-project.supabase.co
SUPABASE_ANON_KEY=your-anon-public-key
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
VIBER_BOT_TOKEN=your-viber-bot-token
CORS_ORIGINS=http://localhost,http://your-frontend.com
ADMIN_USERNAME=admin
ADMIN_PASSWORD=supersecretpassword

> 🛡️ Keep your Supabase Service Role key secret!




---

📦 Requirements

fastapi
uvicorn[standard]
requests
python-dotenv
python-multipart
supabase
pydantic
jinja2

Install dependencies:

pip install -r requirements.txt


---

🔃 Render Deployment

Example render.yaml file for zero-config deployment:

services:

type: web
name: game-viber-backend
env: python
plan: free
buildCommand: "pip install -r requirements.txt"
startCommand: "uvicorn main:app --host 0.0.0.0 --port $PORT"
envVars:

key: SUPABASE_URL
sync: false

key: SUPABASE_ANON_KEY
sync: false

key: SUPABASE_SERVICE_ROLE_KEY
sync: false

key: VIBER_BOT_TOKEN
sync: false

key: CORS_ORIGINS
sync: false

key: ADMIN_USERNAME
sync: false

key: ADMIN_PASSWORD
sync: false




---

🧪 API Usage Examples

Deposit Request

POST /api/v1/deposit
Content-Type: application/json

{
"user_id": "12345",
"amount": 50000,
"slip_url": "https://supabase.co/storage/.../image.jpg"
}

Upload Slip Image

POST /api/v1/slip
Content-Type: multipart/form-data

file: [upload slip image file]

Broadcast Promo Message

POST /api/v1/broadcast
Content-Type: application/json

{
"message": "🔥 Weekend Bonus starts now!",
"users": ["1904720_abc123", "1904720_def456"]
}


---

📄 License

This project is MIT licensed for educational and lab use only.
Do not use for unauthorized automation or production gambling services.


---

> Built with ❤️ for Myanmar 🇲🇲 developers, by EthanVT97
