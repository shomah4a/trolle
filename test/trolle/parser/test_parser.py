#-*- coding:utf-8 -*-

import sys
import io
import unittest

from trolle.parser import parser



class TestParser(unittest.TestCase):
    u'''
    parser モジュールのテスト
    '''

    def test_tokenize(self):
        u'''
        tokenize 関数のテスト
        '''

        fp = io.StringIO(u'''def add(a, b):
    return a + b''')

        sys.stderr.write((str(parser.tokenize(fp, 'test.py'))))
        
