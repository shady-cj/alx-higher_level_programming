#!/usr/bin/python3
"""
Using SQLAlchemy to define a database schema.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    Defining the database schema
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade = "all, delete", backref="state")

