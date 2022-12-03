#!/usr/bin/python3

"""
Issueing a query to fetch the data thats starts with 'a' from a given database
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    url = 'mysql+mysqldb://{}:{}@localhost/{}'\
            .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    session = Session(bind=engine)
    for s in session.query(State).filter(State.name.like("%a%")):
        print(f"{s.id}: {s.name}")
