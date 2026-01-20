from fastapi import APIRouter, Request
from starlette.responses import RedirectResponse, JSONResponse  
from authlib.integrations.starlette_client import OAuth
from config import settings
from urllib.parse import urlparse

router = APIRouter(prefix="/auth", tags=["auth"])

oauth = OAuth()
oauth.register(
  name='google',
  server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
  client_id = settings.client_id,
  client_secret = settings.client_secret,
  client_kwargs = {
    'scope' : "email openid profile",
  }
)

@router.get("/login")
async def login(request: Request):
  expected = urlparse(settings.oauth_redirect_uri)
  if request.url.hostname != expected.hostname:
    target = f"{expected.scheme}://{expected.netloc}/auth/login"
    return RedirectResponse(target)
  redirect_uri = settings.oauth_redirect_uri
  return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/callback", name="auth_callback")
async def callback(request: Request):
  token = await oauth.google.authorize_access_token(request)
  print("auth token", token)
  user = token.get("userinfo")
  if user:
    request.session["user"] = dict(user)
  return RedirectResponse(settings.frontend_url)

@router.get("/me")
async def me(request: Request):
  user = request.session.get("user")
  if not user:
    return JSONResponse({"detail": "not authenticated"}, status_code=401)
  return user

@router.post("/logout")
async def logout(request: Request):
  request.session.pop("user", None)
  return {"ok": True}
