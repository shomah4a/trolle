#-*- coding:utf-8 -*-

import os
import unittest
import tempfile

from trolle.builder import handlers


class TestHandler(unittest.TestCase):
    u'''
    リポジトリを処理するハンドラのテスト
    '''


    def setUp(self):

        self.tmp = tempfile.mkdtemp()


    def tearDown(self):

        os.system('rm -rf ' + self.tmp)
    

    def test_git(self):
        u'''
        git でチェックアウトする
        '''

        repo = 'https://github.com/shomah4a/tornadotest.git'

        handlers._git(repo, self.tmp)

        self.assertTrue(os.path.exists(os.path.join(self.tmp, '.git')))


    def test_mercurial(self):
        u'''
        mercurial でチェックアウトする
        '''

        repo = 'https://bitbucket.org/shomah4a/pypy-tutorial'

        handlers._mercurial(repo, self.tmp)

        self.assertTrue(os.path.exists(os.path.join(self.tmp, '.hg')))
    



    def test_get_handler(self):

        self.assertEqual(handlers.get_handler('git'), handlers._git)
        self.assertEqual(handlers.get_handler('mercurial'), handlers._mercurial)
        self.assertEqual(handlers.get_handler('subversion'), handlers._subversion)

        with self.assertRaises(ValueError):
            handlers.get_handler('hogefugahamspam')
