#-*- coding:utf-8 -*-
u'''
バックグラウンドで動かすジョブ
'''

import os

from trolle import path
from . import handlers



def checkout(proj, root):
    u'''
    チェックアウトする
    '''

    par = os.path.dirname(root)

    if not os.path.exists(par):
        os.makedirs(par)

    handler = handlers.get_handler(proj.repository_type)

    handler(proj.repository_uri, root)



def project_builder(proj):
    u'''
    プロジェクトをチェックアウトしたりしてとってくる
    '''

    root = path.get_respository_by_project(proj)

    checkout(proj, root)

    
