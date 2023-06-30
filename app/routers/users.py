# Python
from typing import List

# FastAPI
from fastapi import status, APIRouter

#Models
from ..models import user

# Initializations
router = APIRouter()

## Users

### Sign Up
@router.post(path="/sign-up", response_model=user.User, status_code=status.HTTP_201_CREATED, summary="Register a User", tags=['Users'])
def sign_up():
    pass

### Login
@router.post(path="/login", response_model=user.User, status_code=status.HTTP_200_OK, summary="Login a User", tags=['Users'])
def login():
    pass

### Show all Users
@router.get(path="/users", response_model=List[user.User], status_code=status.HTTP_200_OK, summary="Show all Users", tags=['Users'])
def show_users():
    pass

### Show User Datails
@router.get(path="/users/{user_id}", response_model=user.User, status_code=status.HTTP_200_OK, summary="Show a User", tags=['Users'])
def show_user():
    pass

### Delete a User
@router.delete(path="/users/{user_id}/delete", response_model=user.User, status_code=status.HTTP_200_OK, summary="Delete a User", tags=['Users'])
def delete_user():
    pass

### Update a User
@router.put(path="/users/{user_id}/update", response_model=user.User, status_code=status.HTTP_200_OK, summary="Update a User", tags=['Users'])
def update_user():
    pass