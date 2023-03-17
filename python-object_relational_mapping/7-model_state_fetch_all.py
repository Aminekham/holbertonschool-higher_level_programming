#!/usr/bin/python3
"""This script lists objects from database using sqlalchemy"""
from model_state import Base, State
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3])
        )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    s = Session()
    rows = s.query(State).order_by(State.id).all()
    for state in rows:
        print("{}: {}".format(state.id, state.name))

    s.close()
