#-*- coding:utf-8 -*-

import os
import sqlalchemy as al
from sqlalchemy import orm, sql

from . import tables


class Session():

    def __init__(self):

        self.session = session()


    def __enter__(self):

        return self.session


    def __exit__(self, *exception):

        if exception[0] is not None:
            self.session.rollback()

        self.session.close()



def initialize(config):

    global engine
    global session
    global meta

    engine = al.create_engine(config.uri, echo=config.echo)

    session = orm.sessionmaker(autocommit=True, autoflush=False)
    session.configure(bind=engine)
    

    tables.Base.metadata.bind = engine
    tables.Base.metadata.create_all()


