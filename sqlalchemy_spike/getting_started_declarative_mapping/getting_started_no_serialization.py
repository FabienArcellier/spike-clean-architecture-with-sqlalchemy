#!/usr/bin/python
# coding=utf-8
import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from sqlalchemy_spike.getting_started_declarative_mapping.model import Base, User


def main():
    ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
    print(json.dumps(ed_user))


if __name__ == "__main__":
    main()
