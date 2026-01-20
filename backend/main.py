from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from api.auth_route import router as auth_route
from api.user_route import router as user_router
from api.chat_route import router as chat_router
from api.message_route import router as message_router
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="add any string...")

app.include_router(auth_route)
app.include_router(user_router)
app.include_router(chat_router)
app.include_router(message_router)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.backend_cors_origin,
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE"],
    allow_headers=["*"],
)