from typing import Optional, List
from random import randrange
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
import psycopg
from psycopg.rows import dict_row
import time
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db
models.Base.metadata.create_all(bind=engine)
from .routers import users, post, auth

app = FastAPI()
while True:
    
    try:
        conn = psycopg.connect(
            host="localhost",
            dbname="FastAPI",
            user="postgres",
            password="peepoo",
            row_factory=dict_row
        )
        cursor = conn.cursor()
        print("Successful in Connection of Database")
        break

    except Exception as error:
        print("Database Connection Failed")
        print("Error:", error)
        time.sleep(2)


app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
@app.get("/")
def root():
    return {"message": "HELL NAH"}
