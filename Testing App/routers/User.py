from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from config import models,oauth2, database
from sqlalchemy.orm import Session

import schemas
from config.hashing import Hash
from Repositories.User import User

router = APIRouter(
	prefix = '/users',
	tags = ['Users'],
	)
get_db = database.get_db

@router.get('/')
def main_page():
	return {'detail':'This is the main page'}

@router.post('/register', response_model = schemas.UserOut,status_code= 201)
def register_user(user:schemas.UserIn, db:Session = Depends(get_db)):
	return User.register_user(user,db)

@router.get('/{id}', response_model = schemas.UserOut)
def get_user_by_id(id: int, db: Session = Depends(get_db),):
	return User.get_user_by_id(id,db)

@router.delete("/delete/{id}")
def delete_user(id:int, db:Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
	return User.delete_user(id,db,current_user)

@router.put('/update/{id}', response_model = schemas.UserOut)
def update_user(id: int, new_user: schemas.UserIn,db:Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
	return User.update_user(id,new_user,db,current_user)



