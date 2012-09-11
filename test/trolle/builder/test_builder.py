#-*- coding:utf-8 -*-

import os
import unittest

from trolle.builder import builder


class Dummy(object):
    pass



class TestBuilder(unittest.TestCase):


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

        os.system('rm -rf /tmp/repos/1')

        
        
