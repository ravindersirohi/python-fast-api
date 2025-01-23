import os, json, requests
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import RedirectResponse
from requests_oauthlib import OAuth2Session
from jose import JWTError, jwt

app = FastAPI()

#Just for testing.
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# OAuth2 Configuration to be moved to env config.
GCP_CLIENT_ID = os.environ.get('GCP_CLIENT_ID')
GCP_CLIENT_SECRET = os.environ.get('GCP_CLIENT_SECRET')
REDIRECT_URI = os.environ.get('REDIRECT_URI')
AUTHORIZATION_BASE_URL = "https://accounts.google.com/o/oauth2/auth"
TOKEN_URL = "https://accounts.google.com/o/oauth2/token"
SCOPE = ["openid", 
         "https://www.googleapis.com/auth/userinfo.email", 
         "https://www.googleapis.com/auth/userinfo.profile"
         ]

# Create an OAuth2 session
oauth = OAuth2Session(GCP_CLIENT_ID, redirect_uri=REDIRECT_URI,scope=SCOPE)

@app.get("/")
def main():
    return "Fast API is up!"

@app.get("/login")
async def login():
    authorization_url, state = oauth.authorization_url(AUTHORIZATION_BASE_URL)
    return RedirectResponse(authorization_url)

@app.get("/callback")
async def callback(request: Request):  
    try:
        # Fetch the token
        token = oauth.fetch_token(
            TOKEN_URL,
            authorization_response=str(request.url),
            client_secret=GCP_CLIENT_SECRET
        )
        return {"token": token}
    except Exception as e:
        # Handle token fetching errors
        error_message = str(e)
        if 'Missing required parameter' in error_message:
            error_details = json.loads(e.response.text)
            return {"error": "Missing required parameter", "details": error_details}
        else:
            return {"error": "Token fetching failed", "details": error_message} 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/protected")
async def protected_route(token: str = Depends(oauth2_scheme)):
    try:
        # Fetch the public keys used to verify the token
        keys_response = requests.get("https://www.googleapis.com/oauth2/v3/certs")
        keys = keys_response.json()
        
        # Decode and verify the token
        payload = jwt.decode(token, keys, algorithms=["RS256"], audience=GCP_CLIENT_ID)
        return {"message": "Access granted", "user_info": payload}
    except JWTError as e:
        raise HTTPException(status_code=401, detail=f"Invalid token: {str(e)}")
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching public keys: {str(e)}")

