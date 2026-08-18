from jose import JWSError, jwt 
from datetime import datetime, timedelta
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