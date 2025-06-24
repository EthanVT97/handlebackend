🎮 Bot Backend API - Viber + Supabase + Chatrace Integration

This repository powers a lightweight FastAPI backend that handles deposit/withdrawal logic, slip uploads, promo broadcasting, and user phone management — built for online game bot systems integrated with Viber and Chatrace.


---

🚀 Features

✅ Deposit & Withdrawal API

✅ Upload payment slips to Supabase Storage

✅ Broadcast messages to Chatrace bot users

✅ Edit user phone numbers from Admin Panel

✅ Built with FastAPI + RESTful architecture

✅ Deployable to Render



---

🧱 Tech Stack

Component	Description

FastAPI	Web framework for backend APIs
Supabase	PostgreSQL, Auth, Storage
Chatrace	Messaging Bot Broadcast System
Render	Hosting with auto-deploy from GitHub



---

📁 API Endpoints

Endpoint	Method	Description

/	GET	Health check
/deposit	POST	Submit deposit with slip
/withdraw	POST	Submit withdrawal request
/broadcast	POST	Send promo messages to bot users
/users	GET	List all users
/users/{game_id}	PUT	Update user phone
/upload-slip	POST	Upload slip image to Supabase Storage



---

⚙️ Environment Variables (.env)

Create .env or .env.example in root:

SUPABASE_URL=https://your-project.supabase.co  
SUPABASE_KEY=your-supabase-service-role-key  
CHATBOT_TOKEN=your-chatrace-api-token  
  
> 🛡️ Warning: Keep your Supabase Service Role key secret!  
  
  
  
  
---  
  
📦 Requirements  
  
fastapi  
uvicorn  
requests  
python-dotenv  
python-multipart  
  
Install with:  
  
pip install -r requirements.txt  
  
  
---  
  
🔃 Render Deployment  
  
Add a render.yaml file for zero-config deploy to render.com:  
  
services:  
  - type: web  
    name: game-viber-backend  
    env: python  
    plan: free  
    buildCommand: "pip install -r requirements.txt"  
    startCommand: "uvicorn main:app --host 0.0.0.0 --port 10000"  
    envVars:  
      - key: SUPABASE_URL  
        sync: false  
      - key: SUPABASE_KEY  
        sync: false  
      - key: CHATBOT_TOKEN  
        sync: false  
  
  
---  
  
🧪 API Testing (Example)  
  
➕ Deposit  
  
POST /deposit  
Content-Type: application/json  
  
{  
  "game_id": "12345",  
  "amount": 50000,  
  "slip_url": "https://supabase.co/storage/.../image.jpg"  
}  
  
📤 Upload Slip (multipart)  
  
POST /upload-slip  
Content-Type: multipart/form-data  
file: [upload slip image]  
  
🔁 Broadcast Message  
  
POST /broadcast  
{  
  "message": "🔥 Weekend Bonus starts now!",  
  "users": ["1904720_abc123", "1904720_def456"]  
}  
  
  
  
---  
  
📄 License  
  
This project is MIT licensed for educational and lab use. Do not use for unauthorized automation.  
  
  
---  
  
> Built with ❤️ for Myanmar 🇲🇲 developers, by EthanVT97
