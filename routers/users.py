# Python
from typing import List
import json

# FastAPI
from fastapi import Body, status, APIRouter

#Models
from models import user

# Initializations
router = APIRouter()

## Users

### Sign Up
@router.post(path="/sign-up", response_model=user.User, status_code=status.HTTP_201_CREATED, summary="Register a User", tags=['Users'])
def sign_up(user: user.UserRegister = Body()):
    """
    **SIGN UP**

    *This path operations register a user in the aplication*

    *Args:* 
    
    - Request Body Parameter:

        - user: UserRegister

    *Returns:*

    - A JSON with the basic user's information
         
        - user_id: UUID
        - email: EmalStr
        - first_name: str
        - last_name: str
        - birth_date: date str
    """
    with open("users.json", "r+", encoding="utf-8") as file:
        results = json.loads(file.read())
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict['user_id'])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
        file.seek(0) # top fo the file
        file.write(json.dumps(results))
        return user

### Login
@router.post(path="/login", response_model=user.User, status_code=status.HTTP_200_OK, summary="Login a User", tags=['Users'])
def login():
    pass

### Show all Users
@router.get(path="/users", response_model=List[user.User], status_code=status.HTTP_200_OK, summary="Show all Users", tags=['Users'])
def show_users():
    """
    **SHOW ALL USERS**

    *This path operation shows all users in the app*

    *Args:* 

        -

    *Returns:*

    - JSON list with all users in the app, with the following keys:

        - user_id: UUID
        - email: EmalStr
        - first_name: str
        - last_name: str
        - birth_date: date str
    """
    with open("users.json", "r", encoding="utf-8") as file:
        results = json.loads(file.read())
        return results

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