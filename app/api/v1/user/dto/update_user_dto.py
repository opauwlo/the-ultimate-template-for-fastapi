from pydantic import BaseModel, validator
from typing import Optional
import re

class UpdateUserDto(BaseModel):
    id: int
    username: Optional[str]
    email: Optional[str]
    password: Optional[str]
    avatar_url: Optional[str]
    avatar_id: Optional[str]
    bio: Optional[str]
    
    @validator('username')
    def check_lenght (cls, v):
        if len(v) > 20:
            raise ValueError('Username must be less than 20 characters')
        return v
            
    @validator('email')
    def check_email (cls, v):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", v):
            raise ValueError('Invalid email')
        return v

        
    
