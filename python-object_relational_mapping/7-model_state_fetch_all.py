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
        sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # associate it with our custom Session class
    Session = sessionmaker()

    # associate it with our custom Session class
    Session.configure(bind=engine)

    session = Session()

    rows = session.query(State).order_by(State.id).all()

    for state in rows:
        print("{}: {}".format(state.id, state.name))

    session.close()
