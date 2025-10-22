import os
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from app.dependencies import init_db
from contextlib import asynccontextmanager
from app.blogs.routers import router as blog_router
from app.auth.routers import router as auth_router
from app.user.routers import router as user_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Startup event running...")
    init_db()
    print("✅ Database initialized.")
    yield
    print("🛑 Shutdown event running...")
    

app = FastAPI(lifespan=lifespan)


load_dotenv() 
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(blog_router)
app.include_router(user_router)
app.include_router(auth_router)