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
        print("The database has entries.")
        return True
    else:
        print("The database is empty.")
        return False
    
def first_player_title():
    if session.query(Player).filter_by(title = 'Duke').order_by(Player.id).first() is not None:
        return 'Duke'
    elif session.query(Player).filter_by(title = 'Architect').order_by(Player.id).first() is not None:
        return 'Architect'
    elif session.query(Player).filter_by(title = 'Scientist').order_by(Player.id).first() is not None:
        return 'Scientist'
    else:
        return 'Justice'