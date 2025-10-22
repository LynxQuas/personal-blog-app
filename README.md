
# Vue + FastAPI

This project contains a **Vue 3 frontend** and a **FastAPI backend**. Follow the steps below to get it running locally.

---

## 1. Clone the repository
```bash
git clone git@github.com:LynxQuas/personal-blog-app.git
```
## 2. Setup Backend (FastAPI)

```bash

cd backend
python3 -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

## 2. Setup Frontend (Vue 3)

```bash
cd frontend
npm install
cp .env.example .env
npm run dev
``` 
