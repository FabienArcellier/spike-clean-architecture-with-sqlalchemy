from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

"""
see: https://docs.sqlalchemy.org/en/13/orm/tutorial.html#declare-a-mapping
"""

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname)
