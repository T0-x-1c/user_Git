from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union


app = FastAPI()

users = {
    "login": "like",
    "age": 18,
    "password" : "123"

}

class User(BaseModel):
    login: str
    password: str
    age: int

@app.get("/users/all")
async def get_all_users():
    '''
    Повертає данны про користувачів
    '''
    return users

@app.post("/users/new")
async def add_new_users(new_user: User):
    '''
    Додає нового користувача з параметрами login, age, password
    '''
    users.append({
        "login": new_user.login,
        "age": new_user.age,
        "password" : new_user.password
    })
    return {"message: 'Користувача додано'"}