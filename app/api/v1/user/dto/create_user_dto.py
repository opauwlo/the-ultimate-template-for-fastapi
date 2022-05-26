from pydantic import BaseModel, validator
from typing import Optional
import re

class CreateUserDto(BaseModel):
    username: str
    email: str
    password: str
    
    @validator('username')
    def check_username (cls, v):
        e = []
        if len(v) > 15:
            e.append('Username must be less than 15 characters')
        if not re.match(r"^[a-zA-Z0-9_]+$", v):
            e.append('Username must be alphanumeric')
        if len(v) < 4:
            e.append('Username must be at least 4 characters')
        if len(e) > 0:
            raise ValueError(', '.join(e))
        return v
    
    @validator('password')
    def check_password (cls, v):
        e = []
        if len(v) < 8:
            e.append('Password must be at least 8 characters')
        if not re.search('[0-9]', v):
            e.append('Password must contain at least one number')
        if not re.search('[A-Z]', v):
            e.append('Password must contain at least one uppercase letter')
        if not re.search('[a-z]', v):
            e.append('Password must contain at least one lowercase letter')
        if not re.search('[!@#$%^&*()]', v):
            e.append('Password must contain at least one special character')
        if len(e) > 0:
            raise ValueError(', '.join(e))
        return v
            
    
    @validator('email')
    def check_email (cls, v):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", v):
            raise ValueError('Invalid email')
        return v

    class Config:
        schema_extra = {
            "example": {
                "username": "admin",
                "email": "email@email.com",
                "password": "passWord123#",
            }
        }   
