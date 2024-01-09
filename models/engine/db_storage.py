#!/usr/bin/python3
"""Incoporating a database storage"""

from models.place import Place
from models.review import Review
from models.base_model import Base
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

user = getenv('HBNB_MYSQL_USER')
pwd = getenv('HBNB_MYSQL_PWD')
host = getenv('HBNB_MYSQL_HOST')
db = getenv('HBNB_MYSQL_DB')
env = getenv('HBNB_ENV')


class DBStorage:
  """DataBase storage"""
  __engine = None
  __session = None
  
  def __init__(self):
    self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                .format(user, pwd, host, db),
                                pool_pre_ping=True) 

    if env == "test":
      Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """  """
        if cls:
            objects = self.__session.query(cls).all()
        else:
            classes = [State, City, User, Place, Review, Amenity]
            objects = []
            for c in classes:
                objects += self.__session.query(c)
        return {"{}.{}".format(type(obj).__name__, obj.id): obj for obj in
                objects}

    def new(self, obj):
        """
        method adds a new object to a pending state of the database
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """ method saves object """
        self.__session.commit()

    def delete(self, obj=None):
        """ method deletes object """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ method reloads all tables """
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()

    def close(self):
        """ method closes DB Session """
        self.__session.close()
