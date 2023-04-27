from fastapi import APIRouter, Request
from ..models.user import SignupData
from ..middlewares.throttling import limiter    
import secrets
router = APIRouter()

users = {}

def generate_api_key():
    """
    Generates a random API key using secrets.token_hex function from the secrets module.
    
    return: A string representing the generated API key.
    """
    api_key = secrets.token_hex(32)
    
    return api_key

@router.post("/register")
@limiter.limit("7/minute")
def register(user: SignupData, request: Request):
    """
    Endpoint for user registration. It receives a SignupData object in the request body, generates a new API key using
    the generate_api_key function, associates it with the user's name, and returns the API key in a dictionary format.
    
    param user: A SignupData object containing the user's name and email in the request body.
    param request: A FastAPI Request object containing the request data.
    return: A dictionary with the API key associated with the user's name.
    """
    api_key = generate_api_key()
    users[user.name] = api_key
    return {"api_key": api_key}

