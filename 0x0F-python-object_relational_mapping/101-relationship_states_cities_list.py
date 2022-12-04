#!/usr/bin/python3

"""
 a script that creates the State “California” with the City “San Francisco”
 from the database passed as command line argument
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State, Base

if __name__ == "__main__":
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    states = session.query(State).all()

    for s in states:
        print(f'{s.id}: {s.name}')
        for city in s.cities:
            print(f"    {city.id}: {city.name}")