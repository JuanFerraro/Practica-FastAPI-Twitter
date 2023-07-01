# Python
from typing import List
import json

# FastAPI
from fastapi import Body, status, APIRouter, Path, HTTPException
from fastapi.responses import JSONResponse

#Models
from models import user

#Utils
from .utils import read_file, write_file, find_in_file

# Initializations
router = APIRouter()

## Users

### Sign Up
@router.post(path="/sign-up", response_model=user.User, status_code=status.HTTP_201_CREATED, summary="Register a User", tags=['Users'])
def sign_up(user: user.UserRegister = Body()):
    """**SIGN UP**

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
    users = read_file("users.json") # Users List
    user_dict = user.dict() # user info to a dict
    user_dict["user_id"] = str(user_dict['user_id']) 
    user_dict["birth_date"] = str(user_dict["birth_date"])
    users.append(user_dict)
    write_file(users, "users.json")
    return user

### Login
@router.post(path="/login", response_model=user.User, status_code=status.HTTP_200_OK, summary="Login a User", tags=['Users'])
def login():
    pass

### Show all Users
@router.get(path="/users", response_model=List[user.User], status_code=status.HTTP_200_OK, summary="Show all Users", tags=['Users'])
def show_users():
    """**SHOW ALL USERS**

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

### Show User Details
@router.get(path="/users/{user_id}", response_model=user.User, status_code=status.HTTP_200_OK, summary="Show a User", tags=['Users'])
def show_user(user_id: str = Path()):
    """**SHOW USER DETAILS**

    Args:
        user_id (str, optional): _This is the user's id the is going to be searched in the aplication_. Defaults to Path().

    Raises:
        HTTPException: _404, This is the status code that shows up if the user is not found_

    Returns:

        User: This is the basic user's information:
            
            - user_id: UUID
            - email: EmalStr
            - first_name: str
            - last_name: str
            - birth_date: date str
    """

    users = read_file("users.json") # Users List
    found = find_in_file(users,"user_id",user_id)
    if found == False:
        raise HTTPException(status_code=404, detail="Person not found")
    else: 
        return found

### Delete a User
@router.delete(path="/users/{user_id}/delete", status_code=status.HTTP_200_OK, summary="Delete a User", tags=['Users'])
def delete_user(user_id: str = Path()):
    """**DELETE A USER**

    *This function delete a user from de aplication using the user_id*

    Args:
        user_id (str, optional): _This is the user id that is going to be deleted_. Defaults to Path().

    Raises:
        HTTPException: _404, this is the status code that show up if the user_id it's not found_

    Returns:
        _JSON_: _With the status code and the message OK_
    """
    users = read_file("users.json")
    for user in users:
        if user['user_id'] == user_id:
            users.remove(user)
            write_file(users, "users.json") 
            return JSONResponse(status_code=200, content='Delete user succesfully')
    raise HTTPException(status_code=404, detail='User not found')

### Update a User
@router.put(path="/users/{user_id}/update", response_model=user.UserRegister, status_code=status.HTTP_200_OK, summary="Update a User", tags=['Users'])
def update_user(user_id: str = Path(), update_user: user.UserRegister = Body()):
    """**UPDATE USER**

    *This function update a user from de aplication using the user_id*

    Args:
        user_id (str, optional): _This is the user id that is going to be update_. Defaults to Path().
        update_user (user.UserRegister, optional): _User information that is going to be updated_. Defaults to Body().
            - email: EmalStr
            - first_name: str
            - last_name: str
            - birth_date: date str
            - password: str
    Raises:
        HTTPException: _404, this is the status code that show up if the user_id it's not found_

    Returns:
        _JSON_: _With the status code and the message OK_
    """ 
    users = read_file("users.json")
    update_user = update_user.dict()
    for user in users:
        if user["user_id"] == user_id:
            user['email'] = update_user['email']
            user['first_name'] = update_user['first_name']
            user['last_name'] = update_user['last_name']
            user['birth_date'] = str(update_user['birth_date'])
            user['password'] = update_user['password']
            write_file(users, "users.json") 
            return JSONResponse(status_code=200, content='Update user succesfully')
    raise HTTPException(status_code=404, detail='User not found')