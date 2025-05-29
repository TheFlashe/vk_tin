import sqlalchemy
from sqlalchemy.orm import sessionmaker
import configparser

from models import create_tables, User, Favorite, Photo, Profile


class ConfigLoader:
    def __init__(self, file_path='config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(file_path)

    def get(self, section, key):
        return self.config[section][key]


conf = ConfigLoader()

DSN = conf.get('DNS', 'link')
vk_token = conf.get('VK_TOKEN', 'token')

engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)

session = Session()

create_tables(engine)

session.close()
