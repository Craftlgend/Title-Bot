from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



#The databasee setup is here
engine = create_engine('sqlite:///player_data.db')  # SQLite database file
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()




# Defining of the model meaning the stucture of the DB
class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    discord_id = Column(String)
    discord_name = Column(String)
    x_coord = Column(Integer)
    y_coord = Column(Integer)
    kingdom_type = Column(String)
    title = Column(String)


    Base.metadata.create_all(engine)


def check_database_has_entries():
    count = session.query(Player).count()
    if count > 0:
        return True
    else:
        return False

def check_if_title_in_database(requested_title):
    count = session.query(Player).filter_by(title = requested_title).count()
    if count > 0:
        return True
    else:
        return False