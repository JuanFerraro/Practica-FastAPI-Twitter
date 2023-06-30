# Python
from typing import List

# FastAPI
from fastapi import status, APIRouter

#Models
from ..models import tweet

# Initializations
router = APIRouter()

## Tweets

### Show all Tweets
@router.get(path="/", response_model=List[tweet.Tweet], status_code=status.HTTP_200_OK, summary="Show all tweets", tags=['Tweets'])
def home():
    return {"Twitter API": "Working"}

### Post a tweet
@router.post(path="/post", response_model=tweet.Tweet, status_code=status.HTTP_201_CREATED, summary="Post a Tweet", tags=['Tweets'])
def post():
    pass

### Show a tweet
@router.get(path="/tweets/{tweet_id}", response_model=tweet.Tweet, status_code=status.HTTP_200_OK, summary="Show a Tweet", tags=['Tweets'])
def show_tweet():
    pass

### Delete a tweet
@router.delete(path="/tweets/{tweet_id}/delete", response_model=tweet.Tweet, status_code=status.HTTP_200_OK, summary="Delete a Tweet", tags=['Tweets'])
def delete_tweet():
    pass

### Update a tweet
@router.put(path="/tweets/{tweet_id}/update", response_model=tweet.Tweet, status_code=status.HTTP_200_OK, summary="Delete a Tweet", tags=['Tweets'])
def update_tweet():
    pass