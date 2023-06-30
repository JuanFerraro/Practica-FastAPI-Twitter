# Python
from typing import List

# FastAPI
from fastapi import FastAPI, status

# Models
from models import User, UserBase, UserLogin, Tweet

# Initializate app
app = FastAPI()

# Home
@app.get(path="/", tags=["home"])
def home():
    return {"Twitter API": "Working"}

# Users

## Sign Up
@app.post(path="/sign-up", response_model=User, status_code=status.HTTP_201_CREATED, summary="Register a User", tags=['Users'])
def sign_up():
    pass

## Login
@app.post(path="/login", response_model=User, status_code=status.HTTP_200_OK, summary="Login a User", tags=['Users'])
def login():
    pass

## Show Users
@app.get(path="/users", response_model=List[User], status_code=status.HTTP_200_OK, summary="Show all Users", tags=['Users'])
def show_users():
    pass

## Show User Datails
@app.get(path="/users/{user_id}", response_model=User, status_code=status.HTTP_200_OK, summary="Show a User", tags=['Users'])
def show_user():
    pass

## Delete a User
@app.delete(path="/users/{user_id}/delete", response_model=User, status_code=status.HTTP_200_OK, summary="Delete a User", tags=['Users'])
def delete_user():
    pass

## Update a User
@app.put(path="/users/{user_id}/update", response_model=User, status_code=status.HTTP_200_OK, summary="Update a User", tags=['Users'])
def update_user():
    pass

# *************************************************************************************** #
# *************************************************************************************** #