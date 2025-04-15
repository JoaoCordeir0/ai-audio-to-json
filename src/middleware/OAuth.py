from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from jwt import PyJWTError
import os

class OAuth:

    oauth = OAuth2PasswordBearer(tokenUrl='/')

    def __init__(self) -> None:
        pass

    def auth(self, token: str = Depends(oauth)):        
        return self.decode_token(token)                 

    def decode_token(self, token: str):                
        try:            
            return jwt.decode(token, os.getenv('JWT_SECRET_KEY'), algorithms=['HS256'], options={'verify_exp': True})            
        except PyJWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid token',
                headers={ 'WWW-Authenticate': 'Bearer' },
            )