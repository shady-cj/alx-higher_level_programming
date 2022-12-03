#!/usr/bin/python3

"""
Queries for fetching data from the cities table on the a database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import State, Base


if __name__ == "__main__":
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url, pool_pre_ping=True, echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # q = session.query(State.name, City.id, City.name)\
    #     .filter(City.state_id == State.id)\
    #     .order_by(City.id).all()
    q = session.query(State, City).join(State).order_by(City.id).all()
    for state, city in q:
        print(f"{state.name}: ({city.id}) {city.name}")
    # for state_name, city_id, city_name in q:
    #     print(f"{state_name}: ({city_id}) {city_name}")
