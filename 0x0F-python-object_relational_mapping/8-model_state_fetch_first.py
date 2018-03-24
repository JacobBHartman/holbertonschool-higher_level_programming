#!/usr/bin/python3
"""
    list one State object from the database
"""


if __name__ == "__main__":

    import sqlalchemy
    from sys import argv
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    first_object = session.query(State).order_by(State.id).first()
    if first_object is not None:
        print("{}: {}".format(first_object.id, first_object.name))
    else:
        print("Nothing")

    session.close()
