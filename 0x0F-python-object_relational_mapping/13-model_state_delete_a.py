#!/usr/bin/python3

"""
Issueing a query that deletes all entry that starts with a in
the database passed through the command line
"""

from model_state import Base, State
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    url = 'mysql+mysqldb://{}:{}@localhost/{}'\
            .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    session = Session(bind=engine)
    states = session.query(State).filter(State.name.like("%a%")).all()

    for s in states:
        session.delete(s)
        session.commit()