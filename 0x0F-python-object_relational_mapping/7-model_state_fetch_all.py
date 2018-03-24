#!/usr/bin/python3
"""
    list all State objects from the database
"""
import SQLAlchemy
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
        print("{}: {}".format(state.id, state.name))
    session.close()
