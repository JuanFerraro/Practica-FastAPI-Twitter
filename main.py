# Python
from typing import List

# FastAPI
from fastapi import FastAPI, status

# Models
from routers import tweets, users

# Initializate app
app = FastAPI()

app.include_router(users.router)
app.include_router(tweets.router)



