#!/usr/bin/python3
"""
Using SQLAlchemy to define a database schema.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
import sys


Base = declarative_base()


class State(Base):
    """
    Defining the database schema
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    url = 'mysql+mysqldb://{}:{}@localhost/{}'\
            .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url, pool_pre_ping=True, echo=True)

    Base.metadata.create_all(engine)
