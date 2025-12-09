# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.core.config import settings
from app.db.session import engine
from app.db.base import Base
from app.users import router as user_router
# IMPORTANT: Import models here so SQLAlchemy "sees" them before creating tables
from app.users import models as user_models

# --- Lifecycle Manager (Startup/Shutdown) ---
# This replaces the old "on_startup" event. It's the modern way to handle DB startup.
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 1. Startup: Create database tables if they don't exist
    async with engine.begin() as conn:
        # This reads the 'users' table definition from models.py and creates it in Postgres
        await conn.run_sync(Base.metadata.create_all)
    
    yield # The application runs here
    
    # 2. Shutdown: (Optional) Close DB connections if needed
    # await engine.dispose()

# --- Initialize App ---
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)

# --- CORS Configuration ---
# This is crucial for React to talk to FastAPI.
# For development, allow ["*"] (everyone). For production, specify your React domain.
origins = [
    "http://localhost:3000", # React (Create-React-App)
    "http://localhost:5173", # React (Vite)
    "*"                      # Allow all (easiest for dev)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allow GET, POST, PUT, DELETE, etc.
    allow_headers=["*"], # Allow Authorization tokens, Content-Type, etc.
)

# --- Include Routers ---
# This connects your 'users' module to the main API
app.include_router(
    user_router.router, 
    prefix=f"{settings.API_V1_STR}/users", 
    tags=["users"]
)

# --- Health Check Route ---
@app.get("/")
async def root():
    return {
        "message": "Welcome to the Research Project ", 
        "docs_url": "http://127.0.0.1:8000/docs"
    }