import email
from turtle import up
from unicodedata import name
from certifi import where
from fastapi import APIRouter
from database.config import connect,meta
from models.user import users
from schemas.users import User
from sqlalchemy import update,delete,select

user = APIRouter()

@user.get("/", tags=['Return all existing users'])
async def read_users_data():
    return connect.execute(users.select()).fetchall()

@user.get("/{id}", tags=['Return first username by id'])
async def read_user_data(id: int):
    exist_id = connect.execute(users.select().where(users.c.id == id)).first()
    
    if exist_id:
        return {"data": exist_id}
    else:   
       return {"error":'This user does not exists.'}

@user.post("/create", tags=['Create users in database'])
async def create_users(user: User):
    exist_email = connect.execute(users.select().where(users.c.email == user.email)).fetchall()
                          
    if exist_email:
        
        return {"error":'This email already exists.'}
    else:      
     connect.execute(users.insert().values(
        name= user.name,
        email= user.email,
        password= user.password   
    ))
    
     return connect.execute(users.select()).fetchall()

@user.put("/update/{id}", tags=['Update users in database'])
async def update_user_by_id(id:int, user: User):
    
    exist_id = connect.execute(users.select().where(users.c.id == user.id)).first()
    print(exist_id)
    if exist_id:
        
        connect.execute(users.update().where(users.c.id == id).values( 
         name= user.name,
         email= user.email,
         password = user.password))
        
        return {"message": "User updated successfully."}
    
    else:
        return {"error": "User not found or doesnt exists."}

@user.delete("/delete/{id}",tags=['Delete users in database'])
async def delete_user_by_id(id: int):
    connect.execute(users.delete().where(users.c.id == id))
    
    return connect.execute(users.select()).fetchall()