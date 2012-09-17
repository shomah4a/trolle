#-*- coding:utf-8 -*-

import os
import sys
import unittest
import tempfile
import copy

from trolle import config


class TestConfig(unittest.TestCase):

    def setUp(self):

        self.old_db = copy.deepcopy(config.db)
        self.old_server = copy.deepcopy(config.server)
        

    def tearDown(self):

        config.db = self.old_db
        config.server = self.old_server

        
    @unittest.skip
    def test_section(self):
        u'''
        設定用のセクションテスト
        '''

        s = config.Section(params=['x', 'y', 'z'],
                           defaults=dict(a=10,
                                         b=20,
                                         d=30,
                                         g='10'),
                           converters=dict(a=int,
                                           b=int,
                                           d=int))

        self.assertEqual(s.x, None)
        self.assertEqual(s.y, None)
        self.assertEqual(s.z, None)
        self.assertEqual(s.a, 10)
        self.assertEqual(s.b, 20)
        self.assertEqual(s.d, 30)
        self.assertEqual(s.g, '10')

        s.a = '10'
        s.b = '20'
        s.x = 'aaaaa'

        self.assertEqual(s.a, 10)
        self.assertEqual(s.b, 20)
        self.assertEqual(s.x, 'aaaaa')

        with self.assertRaises(config.ConfigureError):
            s.xx = 10


    def test_init_config(self):
        u'''
        設定読み込みテスト
        '''

        with tempfile.NamedTemporaryFile() as fp:

            fp.write('''[db]
echo = 0

[server]
port = 8000

[ddd]
aaa = 10
''')
            fp.flush()
            config.init_config(os.path.dirname(fp.name),
                               [fp.name, 'aaaa'])

            self.assertEqual(config.db.echo, 0)
            self.assertEqual(config.server.port, 8000)

        
