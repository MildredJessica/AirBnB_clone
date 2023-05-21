#!/usr/bin/python3
"""This module is for User class."""
from models.base_model import BaseModel

class User(BaseModel):
    """Class represents a User."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
