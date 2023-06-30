# Python
from typing import List
import json

# FastAPI
from fastapi import Body, status, APIRouter

#Models
from models import tweet

# Initializations
router = APIRouter()

## Tweets

### Show all Tweets
@router.get(path="/", response_model=List[tweet.Tweet], status_code=status.HTTP_200_OK, summary="Show all tweets", tags=['Tweets'])
def home():
    """
    **SHOW ALL TWEETS**

    *This path operation shows all TWEETS in the app*

    *Args:* 

        -

    *Returns:*

    - JSON list with all TWEETS in the app, with the following keys:

        - tweet_id: UUID
        - content: str
        - create_at: datetime
        - update_at: Optional datetime
        - by: User
        
    """
    with open("tweets.json", "r", encoding="utf-8") as file:
        results = json.loads(file.read())
        return results

### Post a tweet
@router.post(path="/post", response_model=tweet.Tweet, status_code=status.HTTP_201_CREATED, summary="Post a Tweet", tags=['Tweets'])
def post_tweet(tweet: tweet.Tweet = Body()):
    """
    **POST A TWEET**

    *This path operations post a tweet in the app*

    *Args:* 
    
    - Request Body Parameter:

        - tweet: Tweet

    *Returns:*

    - A JSON with the basic tweet information
         
        - tweet_id: UUID
        - content: str
        - create_at: datetime
        - update_at: Optional datetime
        - by: User
    """
    with open("tweets.json", "r+", encoding="utf-8") as file:
        results = json.loads(file.read())
        tweet_dict = tweet.dict()
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        tweet_dict["created_at"] = str(tweet_dict["created_at"])
        tweet_dict["update_at"] = str(tweet_dict["update_at"])
        tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"]) 
        tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"]) 
        results.append(tweet_dict)
        file.seek(0) # top fo the file
        file.write(json.dumps(results))
        return tweet

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