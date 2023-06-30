# Python
from uuid import UUID
from datetime import datetime
from typing import Optional
from .user import User

# Pydantic
from pydantic import BaseModel, Field

# Tweet Model:
class Tweet(BaseModel):
    tweet_id: UUID = Field()
    content: str = Field(min_length=1, max_length=256)
    created_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field()