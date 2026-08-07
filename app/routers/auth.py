from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session

from .. import database, schemas, models, utils

router=APIRouter(tags=["Auth"])

@router.post('/login')
def login(user_cred: schemas.UserLogin, db:Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email==user_cred.email).first()
    if not user or not utils.verify(user_cred.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Cred")

    #create a token
    #return token
    return {"token":"ex"}