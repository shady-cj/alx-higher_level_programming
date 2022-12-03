#!/usr/bin/python3

"""
Issueing a query that updates an entry in the database
passed through the command line
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
    id_2 = session.query(State).filter(State.id == 2).first()
    if id_2:
        id_2.name = "New Mexico"
        session.commit()
