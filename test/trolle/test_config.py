#-*- coding:utf-8 -*-

import unittest

from trolle import config


class TestConfig(unittest.TestCase):

    def test_section(self):


        s = config.Section('x', 'y', 'z',
                           a='10',
                           b='20',
                           d='30',
                           g=10)

        self.assertEqual(s.x, None)
        self.assertEqual(s.y, None)
        self.assertEqual(s.z, None)
        self.assertEqual(s.a, '10')
        self.assertEqual(s.b, '20')
        self.assertEqual(s.d, '30')
        self.assertEqual(s.g, 10)

        s.a = 10
        s.b = 20
        s.x = 'aaaaa'

        self.assertEqual(s.a, 10)
        self.assertEqual(s.b, 20)
        self.assertEqual(s.x, 'aaaaa')

        with self.assertRaises(config.ConfigureError):
            s.xx = 10

        
