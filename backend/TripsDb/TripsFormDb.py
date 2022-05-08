from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, insert, select


class TripFormsDb:
    def __init__(self, db_connection_string):
        self.__engine__ = create_engine(db_connection_string)
        self.__metadata__ = MetaData()
        self.__initialize_tables__()
        self.__metadata__.create_all(self.__engine__)

    def __initialize_tables__(self):
        self.trips = Table('trips', self.__metadata__,
                           Column('id', Integer(), primary_key=True,
                                  autoincrement=True),
                           Column('direction', String(30), nullable=False),
                           Column('name', String(35), nullable=False),
                           Column('description', String(120), nullable=False))

    def add_new_trip(self, values_dict):
        ins = insert(self.trips).values(values_dict)
        with self.__engine__.connect() as conn:
            conn.execute(ins)

    def show_all_trips(self):
        sel_trips = select([self.trips])
        with self.__engine__.connect() as conn:
            return conn.execute(sel_trips).all()
