#!/usr/bin/python3
"""
This script lists objects from a MySQL database using sqlalchemy.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

def list_states():
    """List all states in the database."""
    if len(sys.argv) < 4:
        print("Usage: python3 script.py <user> <password> <database>")
        return

    user, password, database = sys.argv[1:4]

    engine = create_engine(f"mysql+mysqldb://{user}:{password}@localhost/{database}",
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State).order_by(State.id).all()

    for state in rows:
        print(f"{state.id}: {state.name}")

    session.close()

if __name__ == "__main__":
    list_states()
