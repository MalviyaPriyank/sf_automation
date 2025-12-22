from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from api.user_route import router as user_router
from api.chat_route import router as chat_router

app = FastAPI()

app.include_router(user_router)
app.include_router(chat_router)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.backend_cors_origin,
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE"],
    allow_headers=["*"],
)