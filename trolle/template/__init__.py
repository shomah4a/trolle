#-*- coding:utf-8 -*-
__import__('pkg_resources').declare_namespace(__name__)

import os

from trolle import config


def get_template_dir():
    u'''
    テンプレートのある場所
    '''

    return os.path.join(os.path.dirname(__file__), 'templates')
