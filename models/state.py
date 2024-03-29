#!/usr/bin/python3
""" Definition of class state that inherots from basemodel"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class.

    Attributes:
        name (str): state name.
    """

    name = ""
