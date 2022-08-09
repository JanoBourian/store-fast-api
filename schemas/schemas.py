from pydantic import BaseModel, validator, root_validator
from email_validator import validate_email, EmailNotValidError
from datetime import datetime
from typing import List, Optional

## Colors

class ColorsBase(BaseModel):
    name:str
    description: Optional[str]
    
    @root_validator
    def correct_length_id(cls, values):
        name = values.get("name")
        if len(name) > 0 and len(name)<=10 and name.count(" ") == 0:
            return values
        raise ValueError('Field name in Color is incorrect')

class ColorsIn(ColorsBase):
        
    class Config:
        orm_mode = True

class ColorsOut(ColorsBase):
    id: int

    class Config:
        orm_mode = True

## Clothes

class SizesBase(BaseModel):
    name:str
    description: Optional[str]
    
    @root_validator
    def correct_length_id(cls, values):
        name = values.get("name")
        if len(name) > 0 and len(name)<=10 and name.count(" ") == 0:
            return values
        raise ValueError('Field name in Color is incorrect')

class SizesIn(SizesBase):
        
    class Config:
        orm_mode = True

class SizesOut(SizesBase):
    id: int

    class Config:
        orm_mode = True

## Users

class EmailField(str):
    
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
        
    @classmethod
    def validate(cls, v) -> str:
        try:
            validate_email(v)
            return v
        except EmailNotValidError:
            raise ValueError('Email is not valid')
                    

class BaseUser(BaseModel):
    email: EmailField
    full_name: str
    phone: str
    
    @validator("full_name")
    def validate_correct_full_name(cls, v):
        try: 
            first_name, last_name = v.split(" ")
            return v
        except Exception:
            raise ValueError('Full name is not valid')
                    
    
class UsersSignIn(BaseUser):
    password:str
    
class UsersSignOut(BaseUser):
    id: int
    created_at: datetime
    last_modified_at: datetime
    