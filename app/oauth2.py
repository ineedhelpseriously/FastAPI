from jose import JWSError, jwt 
from datetime import datetime, timedelta
from . import schemas
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme= OAuth2PasswordBearer(tokenUrl='login')
#Secret key
#algo
#expiration time
Secret_key="qwertyuiopasdfghjklzxcvbnm"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode=data.copy()
    expire= datetime.now()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    encoded_jwt=jwt.encode(to_encode, Secret_key, algorithm=ALGORITHM)
    
    return encoded_jwt

def verify_access_token(token:str, credentials_exception):
    try:
        paylod=jwt.decode(token, Secret_key, algorithms=ALGORITHM)
        id: str=paylod.get("user_id")
    
        if id in None:
            raise credentials_exception
    
        token_data=schemas.TokenData(id=id)
    except JWSError:
        raise credentials_exception

def get_curr_user(token: str=Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=
                                            "could not validate creds", headers={"WWW-Auth": "bearer"})
    
    return verify_access_token(token, credentials_exception)