"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- ContactMessage -> "contactmessage" collection
- Project -> "project" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

class ContactMessage(BaseModel):
    name: str = Field(..., description="Sender name")
    email: EmailStr = Field(..., description="Sender email")
    message: str = Field(..., description="Message body")

class Project(BaseModel):
    title: str = Field(..., description="Project title")
    description: Optional[str] = Field(None, description="Short description")
    url: Optional[str] = Field(None, description="Project link")
    tags: List[str] = Field(default_factory=list, description="Tech tags")
