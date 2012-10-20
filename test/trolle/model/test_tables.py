#-*- coding:utf-8 -*-

import unittest
import datetime

import pymysql
from sqlalchemy import exceptions

from trolle.model import tables, session


def mk_dbname():

    return 'trolletest' + datetime.datetime.now().strftime('%Y%m%d%H%M%S')


DUMMY_ID = 100
DUMMY_NAME = 'dummyaaaa'
DUMMY_PROJECT_NAME = 'dummyaaaa'
DUMMY_FILEPATH = '/tmp/aaaa/test.py'


class DummyConfig(object):

    def __init__(self, uri):

        self.uri = uri
        self.echo = True


class TestTables(unittest.TestCase):

    DB_NAME = mk_dbname()
    HOSTNAME = 'localhost'
    USER = 'root'


    def setUp(self):

        conn = pymysql.Connect(self.HOSTNAME, self.USER)
        conn.query('create database %s;' % self.DB_NAME)
        conn.close()

        uri = 'mysql+pymysql://%s@%s/%s' % (self.USER, self.HOSTNAME, self.DB_NAME)

        conf = DummyConfig(uri)

        session.initialize(conf)

        with session.Session() as sess:
            with sess.begin():
                tables.create_user(sess,
                                   id=DUMMY_ID,
                                   name=DUMMY_NAME)

            with sess.begin():
                tables.create_project(sess,
                                      id=DUMMY_ID,
                                      owner_id=DUMMY_ID,
                                      name=DUMMY_NAME,
                                      repository_uri='',
                                      repository_type='')

            with sess.begin():
                tables.create_file(sess,
                                   id=DUMMY_ID,
                                   project_id=DUMMY_ID,
                                   filepath=DUMMY_FILEPATH)


    def test_user(self):
        u'''
        ユーザテーブルの定義テスト
        '''

        name = 'aaaa'

        with session.Session() as sess:
            with sess.begin():
                user = tables.create_user(sess, name=name)

            results = tables.search_user(sess, name=name)
            self.assertEqual(len(results), 1)


    def test_login_info(self):

        service = 'twitter'

        with session.Session() as sess:
            with sess.begin():
                login_info = tables.create_login_info(sess,
                                                      user_id=DUMMY_ID,
                                                      service_name=service,
                                                      service_user_id='aaaa')

            self.assertTrue(tables.is_login_info_exists(sess,
                                                        user_id=DUMMY_ID,
                                                        service_name=service))
            self.assertFalse(tables.is_login_info_exists(sess,
                                                         user_id=DUMMY_ID,
                                                         service_name='bbbbb'))



    def test_project(self):
        u'''
        プロジェクトテーブルの定義テスト
        '''

        name = 'bbbb'

        with session.Session() as sess:
            with sess.begin():
                proj = tables.create_project(sess,
                                             owner_id=DUMMY_ID,
                                             name=name,
                                             repository_uri='',
                                             repository_type='')

            results = tables.search_project(sess, name=name)
            self.assertEqual(len(results), 1)


        # foreign key constraint
        with self.assertRaises(exceptions.IntegrityError):
            with session.Session() as sess:
                with sess.begin():
                    proj = tables.create_project(sess,
                                                 owner_id=10000,
                                                 name=name,
                                                 repository_uri='',
                                                 repository_type='')


    def test_file(self):
        u'''
        ファイルテーブルの定義テスト
        '''

        fpath = 'aaaa'

        with session.Session() as sess:
            with sess.begin():
                f = tables.create_file(sess,
                                       project_id=DUMMY_ID,
                                       filepath=fpath)

            results = tables.search_file(sess, project_id=DUMMY_ID,
                                         filepath=fpath)

            self.assertEqual(len(results), 1)


        # foreign key constraint
        with self.assertRaises(exceptions.IntegrityError):
            with session.Session() as sess:
                with sess.begin():
                    f = tables.create_file(sess,
                                           project_id=DUMMY_ID*100,
                                           filepath=fpath)

        # unique constraint
        with self.assertRaises(exceptions.IntegrityError):
            with session.Session() as sess:
                with sess.begin():
                    f = tables.create_file(sess,
                                           project_id=DUMMY_ID,
                                           filepath=fpath)


    def test_tag(self):
        u'''
        タグテーブルの定義テスト
        '''

        name = 'tag'

        with session.Session() as sess:
            with sess.begin():
                t = tables.create_tag(sess,
                                      file_id=DUMMY_ID,
                                      identifier=name,
                                      line=10,
                                      column=10,
                                      type='definition')

            results = tables.search_tag(sess,
                                        identifier=name,
                                        type='definition')
            self.assertEqual(len(results), 1)


        # foreign key constraint
        with self.assertRaises(exceptions.IntegrityError):
            with session.Session() as sess:
                with sess.begin():
                    t = tables.create_tag(sess,
                                          file_id=DUMMY_ID*20,
                                          identifier=name,
                                          line=10,
                                          column=10,
                                          type='definition')

        # unique constraint
        with self.assertRaises(exceptions.IntegrityError):
            with session.Session() as sess:
                with sess.begin():
                    t = tables.create_tag(sess,
                                          file_id=DUMMY_ID,
                                          identifier=name,
                                          line=10,
                                          column=10,
                                          type='definition')

    def test_comment(self):
        u'''
        コメントテーブルの定義テスト
        '''

        with session.Session() as sess:
            with sess.begin():
                c = tables.create_comment(sess,
                                          user_id=DUMMY_ID,
                                          file_id=DUMMY_ID,
                                          line=10,
                                          text=u'commentaaaaa')

            results = tables.search_comment(sess,
                                            user_id=DUMMY_ID,
                                            file_id=DUMMY_ID,
                                            line=10)

            self.assertEqual(len(results), 1)


        # foreign key constraint(user_id)
        with self.assertRaises(exceptions.IntegrityError):
            with session.Session() as sess:
                with sess.begin():
                    c = tables.create_comment(sess,
                                              user_id=1321251,
                                              file_id=DUMMY_ID,
                                              line=10,
                                              text=u'commentaaaaa')

        # foreign key constraint(user_id)
        with self.assertRaises(exceptions.IntegrityError):
            with session.Session() as sess:
                with sess.begin():
                    c = tables.create_comment(sess,
                                              user_id=DUMMY_ID,
                                              file_id=6698768,
                                              line=10,
                                              text=u'commentaaaaa')


        # unique key constraint
        with self.assertRaises(exceptions.IntegrityError):
            with session.Session() as sess:
                with sess.begin():
                    c = tables.create_comment(sess,
                                              user_id=DUMMY_ID,
                                              file_id=DUMMY_ID,
                                              line=10,
                                              text=u'commentaaaaa')

    def tearDown(self):

        conn = pymysql.Connect(self.HOSTNAME, self.USER)
        conn.query('drop database %s;' % self.DB_NAME)
        conn.close()


