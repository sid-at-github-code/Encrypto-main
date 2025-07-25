import redis
from dotenv import load_dotenv
import os
import requests
import secrets
from urllib.parse import urlencode


REDIRECT_URI = "http://localhost:5000/dev/callback"
try:
    # Load .env variables
    load_dotenv()

    # Redis URL
    my_redis_url = os.environ.get("REDIS_URL")
    if not my_redis_url:
        raise ValueError("REDIS_URL not found in .env")

    # Google Client ID
    GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
    if not GOOGLE_CLIENT_ID:
        raise ValueError("GOOGLE_CLIENT_ID not found in .env")

    # Google Client Secret
    GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
    if not GOOGLE_CLIENT_SECRET:
        raise ValueError("GOOGLE_CLIENT_SECRET not found in .env")

    # Redis client
    r = redis.Redis.from_url(my_redis_url)

except Exception as e:
    print({"error": f"❌ Failed to load env vars or connect to Redis: {str(e)}"})
   


def get_google_auth_url():
    params = {
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": "openid email profile",
        "access_type": "offline",
        "prompt": "consent"
    }
    return f"https://accounts.google.com/o/oauth2/v2/auth?{urlencode(params)}"

def exchange_code_for_token(code: str):
    token_url = "https://oauth2.googleapis.com/token"
    data = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code"
    }
    response = requests.post(token_url, data=data)
    return response.json()

def get_user_info(access_token: str):
    headers = {"Authorization": f"Bearer {access_token}"}
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    response = requests.get(userinfo_url, headers=headers)
    return response.json()

def register_or_login_user(user: dict):
    email = user["email"]
    key = f"user:{email}"
    if not r.exists(key):
        r.hset(key, mapping={
            "email": user["email"],
            "name": user.get("name", ""),
            "picture": user.get("picture", "")
        })
    r.expire(key, 864000)  # Set TTL to 10 days
    return key
