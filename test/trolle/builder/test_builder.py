#-*- coding:utf-8 -*-

import os
import copy
import unittest

from trolle.builder import builder
from trolle import config, exceptions


class Dummy(object):
    pass



class TestBuilder(unittest.TestCase):


    def setUp(self):

        self.old_general = config.general
        config.general = copy.deepcopy(config.general)


    def tearDown(self):

        config.general = self.old_general

        os.system('rm -rf /tmp/repos')


    def test_checkout_git(self):
        u'''
        git でチェックアウト
        '''

        obj = Dummy()
        obj.owner_id = 1
        obj.id = 10
        obj.repository_uri = 'https://github.com/shomah4a/tornadotest.git'
        obj.repository_type = 'git'

        root = '/tmp/repos/1/10'

        builder.checkout(obj, root)

        self.assertTrue(os.path.exists('/tmp/repos/1/10'))


    def test_build_project(self):
        u'''
        プロジェクトをビルドする
        '''

        obj = Dummy()
        obj.owner_id = 1
        obj.id = 10
        obj.repository_uri = 'https://github.com/shomah4a/tornadotest.git'
        obj.repository_type = 'git'

        root = '/tmp/repos'

        config.general.repository = root

        # builder.build_project(obj)

        # self.assertTrue(os.path.exists('/tmp/repos/1/10'))


    def test_checkout_error(self):
        u'''
        チェックアウト時のエラー
        '''

        obj = Dummy()
        obj.owner_id = 1
        obj.id = 12
        obj.repository_uri = 'https://github.com/'
        obj.repository_type = 'mercurial'

        root = '/tmp/repos'

        with self.assertRaises(exceptions.CheckoutError):
            builder.build_project(obj)


