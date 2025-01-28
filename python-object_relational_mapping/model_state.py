#!/usr/bin/python3
"""
Contains the class definition of a State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create instance of declarative base
Base = declarative_base()


class State(Base):
    """
    State class that inherits from Base
    Links to MySQL table 'states'
    """
    # Define table name
    __tablename__ = 'states'

    # Define columns
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
