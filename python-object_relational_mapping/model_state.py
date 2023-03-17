#!/usr/bin/python3
"""using the sqlalchemy library to manipulate and create tables"""
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """The states table creation"""
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)