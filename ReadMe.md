# 🌱 Agri-Ai: AI Agriculture Monitoring System

Agri-Ai is a full-stack AI platform designed to help farmers detect plant diseases, pests, and weeds in real-time. It uses a custom-trained **YOLOv9** model for vision detection and **FastAPI / React** for a seamless user experience.

### Model Details
- **Detects:** Weeds, Pests, and Diseases
- **Architecture:** YOLOv9-C (trained for 43 epochs)
- **Dataset:** 7,447 Train / 1,886 Validation / 1,407 Test Images
- **Performance:** mAP50: 0.88 | Precision: 0.91 | Recall: 0.84

---

## 📋 Prerequisites

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.9 – 3.11 | Backend runtime |
| Node.js | 18+ | Frontend runtime |
| npm | 9+ | Frontend package manager |
| Git | Any | Source control |

> **Note:** A CUDA-capable GPU is recommended for faster YOLOv9 inference, but the system falls back to CPU automatically.

---

## 📁 Project Structure

```
Agri-bot-system/
├── backend/       # FastAPI server (port 8000)
│   ├── main.py
│   ├── routers/
│   ├── services/
│   ├── model_weights/   # agri_model.pt lives here
│   ├── requirements.txt
│   └── .env
└── frontend/      # React + Vite app (port 5173)
    ├── src/
    ├── package.json
    └── vite.config.js
```

---

## ⚙️ One-Time Setup

### 1. Clone the Repository

```powershell
git clone <your-repo-url>
cd "Agri-bot-system"
```

### 2. Backend Setup

```powershell
cd backend

# Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install all dependencies
pip install -r requirements.txt
```

#### Configure Environment Variables

The `.env` file in `backend/` must contain the following keys:

```env
OPENAI_API_KEY=<your-openai-key>
GEMINI_API_KEY=<your-gemini-key>
NEWS_API_KEY=<your-news-api-key>
OPENWEATHER_API_KEY=<your-openweather-api-key>
MONGODB_URI=<your-mongodb-connection-string>
MONGODB_DB_NAME=agribot
```

> ⚠️ **Never commit your `.env` file.** It is already listed in `.gitignore`.

#### Model Weights

Ensure `agri_model.pt` is present at:

```
backend/model_weights/agri_model.pt
```

If missing, download it from your shared drive / team storage and place it there.

### 3. Frontend Setup

```powershell
cd ../frontend
npm install
```

---

## 🚀 Running the Application

### Terminal 1 — Start the Backend

```powershell
cd "Agri-bot-system\backend"
.\venv\Scripts\Activate.ps1
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

✅ Backend is ready when you see: `Uvicorn running on http://0.0.0.0:8000`

---

### Terminal 2 — Start the Frontend

```powershell
cd "Agri-bot-system\frontend"
npm run dev
```

✅ Frontend is ready when you see: `➜  Local:   https://localhost:5173/`

> **📱 Mobile Testing Note:** If you want to use the live camera on your phone, check the terminal for the `Network: https://<your-ip>:5173/` address. Open that exact HTTPS address on your mobile phone (connected to the same Wi-Fi) and accept the security warning to give the browser camera permissions!

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/api/detect` | Upload image for crop disease detection |
| POST | `/api/chat` | Chatbot query (Gemini AI) |
| POST | `/api/auth/login` | User login |
| POST | `/api/auth/register` | User registration |
| GET | `/api/recommendations` | Crop recommendations |
| GET | `/api/market` | Market price data |
| GET | `/api/weather?lat=<lat>&lon=<lon>` | Real-time weather + 5-day forecast |

Interactive API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🛠️ Troubleshooting

- **Backend won't start:** Make sure the virtual environment is activated (`.\venv\Scripts\Activate.ps1`) and keys are set in `backend/.env`. Check Python version: `python --version` (needs 3.9–3.11).
- **Detection returns 503 error:** The model file `backend/model_weights/agri_model.pt` is missing or corrupt.
- **Frontend can't reach the backend:** Confirm backend is running on port **8000** and check `frontend/vite.config.js` proxy settings.
- **MongoDB connection error:** Verify `MONGODB_URI` logic and check if your IP is whitelisted in MongoDB Atlas → **Network Access**.
- **PowerShell execution policy error:** Run `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`.

---

## 📦 Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React 18, Vite, React Router, Axios |
| Backend | FastAPI, Uvicorn, Python |
| AI / ML | YOLOv9 (`agri_model.pt`), Google Gemini |
| Database | MongoDB Atlas |
| Auth | JWT / MongoDB users |

---
*Last updated: March 31, 2026*