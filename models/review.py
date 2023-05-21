#!/usr/bin/python3
"""This module is for Review class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """class represents a review."""

    place_id = ""
    user_id = ""
    text = ""
