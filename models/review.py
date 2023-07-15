#!/usr/bin/python3
"""
Defines the Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Reviews that clients put about a place"""
    place_id = ""
    user_id = ""
    text = ""