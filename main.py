import sqlalchemy
from sqlalchemy.orm import sessionmaker
import configparser

from models import create_tables, User, Favorite, Photo, Profile


def load_conf(file_path='config.ini'):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config['DNS']['link']


DSN = load_conf('config.ini')

engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)

session = Session()

create_tables(engine)

session.close()
