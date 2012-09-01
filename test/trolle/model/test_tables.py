#-*- coding:utf-8 -*-

from trolle.model import tables
import pymysql

import unittest
import datetime


from sqlalchemy import exceptions


def mk_dbname():

    return 'trolletest' + datetime.datetime.now().strftime('%Y%m%d%H%M%S')


DUMMY_ID = 100
DUMMY_NAME = 'dummyaaaa'
DUMMY_PROJECT_NAME = 'dummyaaaa'
DUMMY_FILEPATH = '/tmp/aaaa/test.py'


class TestTables(unittest.TestCase):

    DB_NAME = mk_dbname()
    HOSTNAME = 'localhost'
    USER = 'root'


    def setUp(self):

        conn = pymysql.Connect(self.HOSTNAME, self.USER)
        conn.query('create database %s;' % self.DB_NAME)
        conn.close()

        uri = 'mysql+pymysql://%s@%s/%s' % (self.USER, self.HOSTNAME, self.DB_NAME)

        conf = tables.DBConfig(uri)

        tables.initialize(conf)

        with tables.Session() as sess:
            tables.create_user(sess,
                               id=DUMMY_ID,
                               name=DUMMY_NAME)

        with tables.Session() as sess:
            tables.create_project(sess,
                                  id=DUMMY_ID,
                                  owner_id=DUMMY_ID,
                                  name=DUMMY_NAME,
                                  repository_uri='',
                                  repository_type='')

        with tables.Session() as sess:
            tables.create_file(sess,
                               id=DUMMY_ID,
                               project_id=DUMMY_ID,
                               filepath=DUMMY_FILEPATH)


    def test_user(self):

        name = 'aaaa'

        with tables.Session() as sess:
            user = tables.create_user(sess, name=name)

        with tables.Session() as sess:
            results = tables.search_user(sess, name=name)
            self.assertEqual(len(results), 1)


    def test_project(self):

        name = 'bbbb'

        with tables.Session() as sess:
            proj = tables.create_project(sess,
                                         owner_id=DUMMY_ID,
                                         name=name,
                                         repository_uri='',
                                         repository_type='')

        with tables.Session() as sess:
            results = tables.search_project(sess, name=name)
            self.assertEqual(len(results), 1)


        # foreign key constraint
        with self.assertRaises(exceptions.IntegrityError):
            with tables.Session() as sess:
                proj = tables.create_project(sess,
                                             owner_id=10000,
                                             name=name,
                                             repository_uri='',
                                             repository_type='')


    def tearDown(self):

        conn = pymysql.Connect(self.HOSTNAME, self.USER)
        conn.query('drop database %s;' % self.DB_NAME)
        conn.close()


