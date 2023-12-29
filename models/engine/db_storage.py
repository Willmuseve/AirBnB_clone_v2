#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """Class Docs"""

    __engine = None
    __session = None

    def __init__(self):
        """Function Docs"""
        hb_user = getenv("HBNB_MYSQL_USER")
        hb_pwd = getenv("HBNB_MYSQL_PWD")
        hb_host = getenv("HBNB_MYSQL_HOST")
        hb_db = getenv("HBNB_MYSQL_DB")
        hb_env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            f"mysql+mysqldb://{hb_user}:{hb_pwd}@{hb_host}/{hb_db}",
            pool_pre_ping=True,
        )

        if hb_env == "test":
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        """ reload method """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
        self.__session = Session()

    def all(self, cls=None):
        """
        query all classes or specific one
        """
        all_classes = [User, Place, State, City, Amenity, Review]
        result = {}

        if cls is not None:
            if isinstance(cls, str):
                cls = eval(cls)
            table_name = cls.__table__.name
            for obj in self.__session.query(cls).all():
                class_name = obj.__class__.__name__
                key_name = f"{class_name}.{obj.id}"
                result[key_name] = obj
        else:
            for cls in all_classes:
                table_name = cls.__table__.name
                for obj in self.__session.query(cls).all():
                    class_name = obj.__class__.__name__
                    key_name = f"{class_name}.{obj.id}"
                    result[key_name] = obj

        return result

    def new(self, obj):
        """add new obj"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def close(self):
        """
        Closes the session
        """
        self.__session.close()
        self.reload()
