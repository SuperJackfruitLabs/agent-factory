from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    # Implement user authentication logic here
    # For now, we'll just return a dummy user
    return {"id": "user123", "username": "testuser"}
