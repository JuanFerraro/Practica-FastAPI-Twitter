# Python
from typing import List
import json

# FastAPI
from fastapi import Body, status, APIRouter, HTTPException, Path
from fastapi.responses import JSONResponse

#Models
from models import tweet

#Utils
from .utils import read_file, write_file, find_in_file

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
    """**POST A TWEET**

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
    tweets = read_file("tweets.json") # Users List
    tweet_dict = tweet.dict() # user info to a dict
    tweet_dict = tweet.dict()
    tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
    tweet_dict["created_at"] = str(tweet_dict["created_at"])
    tweet_dict["update_at"] = str(tweet_dict["update_at"])
    tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"]) 
    tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"]) 
    tweets.append(tweet_dict)
    write_file(tweets, "tweets.json")

    return tweet

### Show a tweet
@router.get(path="/tweets/{tweet_id}", response_model=tweet.Tweet, status_code=status.HTTP_200_OK, summary="Show a Tweet", tags=['Tweets'])
def show_tweet():
    pass

### Delete a tweet
@router.delete(path="/tweets/{tweet_id}/delete", response_model=tweet.Tweet, status_code=status.HTTP_200_OK, summary="Delete a Tweet", tags=['Tweets'])
def delete_tweet(tweet_id: str = Path()):
    """**DELETE A TWEET**

    *This function delete a TWEET from de aplication using the tweet_id*

    Args:
        tweet_id (str, optional): _This is the tweet id that is going to be deleted_. Defaults to Path().

    Raises:
        HTTPException: _404, this is the status code that show up if the tweet_id it's not found_

    Returns:
        _JSON_: _With the status code and the message OK_
    """
    tweets = read_file("tweets.json")
    for tweet in tweets:
        if tweet['user_id'] == tweet_id:
            tweets.remove(tweet)
            write_file(tweets, "tweets.json") 
            return JSONResponse(status_code=200, content='Delete tweet succesfully')
    raise HTTPException(status_code=404, detail='Tweet not found')

### Update a tweet
@router.put(path="/tweets/{tweet_id}/update", response_model=tweet.Tweet, status_code=status.HTTP_200_OK, summary="Update a Tweet", tags=['Tweets'])
def update_tweet(tweet_id: str = Path(), update_tweet: tweet.Tweet = Body()):
    """**UPDATE TWEET**

    *This function update a tweet from de aplication using thetweetr_id*

    Args:
        tweet_id (str, optional): _This is the tweet id that is going to be update_. Defaults to Path().
        
    Raises:
        HTTPException: _404, this is the status code that show up if the tweet_id it's not found_

    Returns:
        _JSON_: _With the status code and the message OK_
            - tweet_id: UUID
            - content: str
            - create_at: datetime
            - update_at: Optional datetime
            - by: User
    """ 
    tweets = read_file("tweets.json")
    update_tweet = update_tweet.dict()
    for tweet in tweets:
        if tweet["tweet_id"] == tweet_id:
            tweet['content'] = update_tweet['content']
            tweet["created_at"] = str(update_tweet["created_at"])
            tweet["update_at"] = str(update_tweet["update_at"])
            tweet["by"]["user_id"] = str(update_tweet["by"]["user_id"]) 
            tweet["by"]["birth_date"] = str(update_tweet["by"]["birth_date"]) 
            write_file(tweets, "tweets.json") 
            return JSONResponse(status_code=200, content='Update tweet succesfully')
    raise HTTPException(status_code=404, detail='Tweet not found')