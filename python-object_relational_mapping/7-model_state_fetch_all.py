#!/usr/bin/python3
"""This script lists objects from database using sqlalchemy"""
from model_state import Base, State
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost/{}"
                           .format(sys.argv[0], sys.argv[1], sys.argv[2]))
    sess = sessionmaker(bind=engine)
    s = sess()
    r = s.query(State).order_by(State.id).all()
    for i in r:
        print("{}: {}".format(i.id, i.name))
    s.close()
