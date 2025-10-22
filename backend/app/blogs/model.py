from sqlmodel import SQLModel, Field as ModelField
from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime, timezone

class Blog(SQLModel, table=True):
    id: Optional[int] = ModelField(default=None, primary_key=True)
    title: str = ModelField(index=True)
    description: str
    content: str
    image_url: str
    created_at: datetime = ModelField(default_factory=lambda: datetime.now(timezone.utc)) 
    updated_at: datetime = ModelField(default_factory=lambda: datetime.now(timezone.utc)) 

class BlogCreateSchema(BaseModel):
    title: str 
    description: str
    content: str 
    image_url: str 
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc)) 

    @field_validator("title", "description", "content", "image_url")
    def not_empty(cls, v, info):
        if not v.strip():
            print(v)
            raise ValueError(f"{info.field_name} cannot be empty or whitespace")
        return v 

class BlogUpdateSchema(BaseModel):
    title: str
    description: str
    content: str
    image_url: str
    
    @field_validator("title", "description", "content", "image_url")
    def not_empty(cls, v, info):
        if not v.strip():
            print(v)
            raise ValueError(f"{info.field_name} cannot be empty or whitespace")
        return v  
