#-*- coding:utf-8 -*-

import unittest

from trolle import utils



class TestEQ(utils.SlotEqual):

    __slots__ = ['a', 'b', 'c', 'd']

    def __init__(self, a, b, c, d):

        self.a = a
        self.b = b
        self.c = c
        self.d = d


class TestEQDerived(TestEQ):

    __slots__ = ['a', 'b', 'c', 'd', 'e']

    def __init__(self, a, b, c, d, e):

        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e



class TestEQ2(utils.SlotEqual):
    pass




class TestSlotEqual(unittest.TestCase):
    u'''
    SlotEqual のテスト
    '''


    def test_eq(self):
        u'''
        同値のテスト
        '''

        a = TestEQ(1, 2, 3, 4)
        b = TestEQ(1, 2, 3, 4)
        c = TestEQ(1, 2, 3, 5)
        d = TestEQDerived(1, 2, 3, 4, 5)
        e = TestEQ2()
        

        self.assertEqual(a, b)
        self.assertEqual(a, a)
        self.assertNotEqual(a, c)
        self.assertNotEqual(a, d)
        self.assertNotEqual(a, e)


