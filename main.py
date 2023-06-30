# FastAPI
from fastapi import FastAPI

# Models
from models import user

app = FastAPI()

# Home
@app.get(path="/", tags=["home"])
def home():
    return {"Twitter API": "Working"}