#!/usr/bin/python3

"""
Issueing a query to fetch the data thats equals the name
passed the command line from a given database
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
    result = session.query(State).filter(text("states.name=:name")).\
        params(name=sys.argv[4]).first()
    if result:
        print(result.id)
    else:
        print("Not found")
