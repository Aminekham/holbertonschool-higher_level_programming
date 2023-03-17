#!/usr/bin/python3
"""
Using sqlalchemy to build the data schema 
"""
import sys
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()


class State(Base):
    """
    create a db using python oop
    """
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))
Base.metadata.create_all(engine)
