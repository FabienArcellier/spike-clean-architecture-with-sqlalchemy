#!/usr/bin/python
# coding=utf-8
import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from sqlalchemy_spike.getting_started_declarative_mapping.model import Base, User


def main():
    user = User()  # A class may be instanciated without arguments
    print(user)

    ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
    print(ed_user)

    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    SessionFactory = sessionmaker()
    SessionFactory.configure(bind=engine)
    session = SessionFactory()  # type: Session
    session.add(ed_user)
    session.commit()
    print(ed_user)

    ed_user.name = "Bob"
    print(ed_user)

    print(json.dumps(ed_user))


if __name__ == "__main__":
    main()
