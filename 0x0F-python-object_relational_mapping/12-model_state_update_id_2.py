#!/usr/bin/python3
"""
    list all State objects from the database
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

    desired_state = session.query(State).filter_by(id=2).first()
    desired_state.name = "New Mexico"

    session.commit()
    session.close()
