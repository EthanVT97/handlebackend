# HandleBackend

A FastAPI-based backend service for financial transaction management, user operations, and Viber bot integration with broadcast messaging capabilities.

## 🚀 Features

- **User Management**: Registration, authentication, and profile management
- **Financial Operations**: Secure deposit and withdrawal processing
- **File Upload**: Payment slip upload and verification
- **Viber Integration**: Bot control and user registration
- **Broadcast System**: Message broadcasting to multiple users
- **Phone Management**: Phone number verification and management

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **Language**: Python 3.8+
- **Template Engine**: Jinja2
- **Environment**: Python-dotenv
- **External APIs**: ChatRace API for messaging

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/EthanVT97/handlebackend.git
cd handlebackend
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Environment Configuration**
```bash
cp .env.example .env
```

Edit `.env` file with your configuration:
```env
# API Configuration
CHATBOT_TOKEN=your_chatrace_api_token

# CORS Configuration
CORS_ORIGINS=http://localhost:3000,https://yourdomain.com

# Database Configuration (if applicable)
DATABASE_URL=your_database_url

# Security
SECRET_KEY=your_secret_key_here
```

5. **Create required directories**
```bash
mkdir -p static templates
```

## 🚀 Running the Application

### Development
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Production
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

## 📡 API Endpoints

### User Management
- `POST /api/v1/user/register` - User registration
- `POST /api/v1/user/login` - User authentication
- `GET /api/v1/user/profile` - Get user profile

### Financial Operations
- `POST /api/v1/deposit/` - Process deposit
- `POST /api/v1/withdraw/` - Process withdrawal
- `GET /api/v1/deposit/history` - Deposit history
- `GET /api/v1/withdraw/history` - Withdrawal history

### File Management
- `POST /api/v1/slip/upload` - Upload payment slip
- `GET /api/v1/slip/{slip_id}` - Get slip details

### Viber Integration
- `POST /api/v1/bot/webhook` - Viber webhook endpoint
- `POST /api/v1/viber/register` - Register Viber user

### Broadcasting
- `POST /api/v1/broadcast/` - Send broadcast message

### Phone Management
- `POST /api/v1/phone/verify` - Verify phone number
- `GET /api/v1/phone/status` - Check verification status

## 🐳 Docker Deployment

### Build Docker Image
```bash
docker build -t handlebackend .
```

### Run Container
```bash
docker run -d \
  --name handlebackend \
  -p 8000:8000 \
  -e CHATBOT_TOKEN=your_token \
  -e CORS_ORIGINS=https://yourdomain.com \
  handlebackend
```

### Docker Compose
```yaml
version: '3.8'
services:
  backend:
    build: .
    ports:
      - "8000:8000"
    environment:
      - CHATBOT_TOKEN=${CHATBOT_TOKEN}
      - CORS_ORIGINS=${CORS_ORIGINS}
    volumes:
      - ./static:/app/static
      - ./templates:/app/templates
```

## ☁️ Cloud Deployment

### Render
```yaml
# render.yaml
services:
  - type: web
    name: handlebackend
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn main:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: CHATBOT_TOKEN
        sync: false
      - key: CORS_ORIGINS
        value: https://yourapp.onrender.com
```

## 🔒 Security Features

- **CORS Protection**: Configurable origin whitelist
- **Environment Variables**: Sensitive data in .env
- **Static File Serving**: Secure static file handling
- **Template Security**: Jinja2 template rendering

## 📁 Project Structure

```
handlebackend/
├── main.py                 # FastAPI application entry point
├── routers/               # API route handlers
│   ├── __init__.py
│   ├── user_router.py     # User management
│   ├── deposit_router.py  # Deposit operations
│   ├── withdraw_router.py # Withdrawal operations
│   ├── broadcast_router.py # Message broadcasting
│   ├── phone_router.py    # Phone verification
│   ├── upload_router.py   # File uploads
│   ├── viber_bot_router.py # Viber bot control
│   └── viber_user_register_router.py # Viber registration
├── static/                # Static files (CSS, JS, images)
├── templates/             # Jinja2 templates
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── Dockerfile            # Docker configuration
└── README.md             # This file
```

## 🧪 Testing

### Run Tests
```bash
pytest tests/ -v
```

### Test Coverage
```bash
pytest --cov=. --cov-report=html
```

### API Testing with curl
```bash
# Test broadcast endpoint
curl -X POST "http://localhost:8000/api/v1/broadcast/" \
  -H "Content-Type: application/json" \
  -d '{"message": "Test message", "users": [1, 2, 3]}'

# Test file upload
curl -X POST "http://localhost:8000/api/v1/slip/upload" \
  -F "file=@payment_slip.jpg"
```

## 📊 Monitoring

### Health Check
```bash
curl http://localhost:8000/health
```

### Metrics Endpoint
```bash
curl http://localhost:8000/metrics
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 Requirements.txt

```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
python-multipart==0.0.6
jinja2==3.1.2
python-dotenv==1.0.0
requests==2.31.0
aiofiles==23.2.1
```

## 🔧 Development Commands

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Format code
black .
isort .

# Lint code
flake8 .
pylint **/*.py

# Type checking
mypy .

# Security scan
bandit -r .
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Issues**: [GitHub Issues](https://github.com/EthanVT97/handlebackend/issues)
- **Documentation**: [Wiki](https://github.com/EthanVT97/handlebackend/wiki)
- **Email**: info@ygnb2b.com

## 🔄 Changelog

### v1.0.0 (2024-12-XX)
- Initial release
- User management system
- Financial transaction processing
- Viber bot integration
- Broadcast messaging system
- File upload functionality

---

⭐ **Star this repository if you find it helpful!**
