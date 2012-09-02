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
        else:
            self.session.commit()

        self.session.close()



class DBConfig(object):
    u'''
    DB の設定
    '''

    def __init__(self, uri, auto_commit=False):

        self.uri = uri
        self.auto_commit = auto_commit


    def get_uri(self):

        return self.uri


    def get_auto_commit(self):

        return self.auto_commit


def initialize(config):

    global engine
    global session
    global meta

    uri = config.get_uri()

    engine = al.create_engine(uri, echo=True)

    session = orm.sessionmaker(autocommit=config.get_auto_commit())
    session.configure(bind=engine)
    

    tables.Base.metadata.bind = engine
    tables.Base.metadata.create_all()


