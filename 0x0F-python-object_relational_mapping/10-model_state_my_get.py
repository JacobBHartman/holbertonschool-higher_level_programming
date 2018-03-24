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
    state_we_want = argv[4]
    flag = 0
    for state in session.query(State).order_by(State.id).all():
        if state_we_want == state.name:
            print(state.id)
            flag += 1
    if flag == 0:
        print("Not found")
    session.close()
