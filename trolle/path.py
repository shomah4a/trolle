#-*- coding:utf-8 -*-
u'''
サーバ上のパスを扱う
'''

import os

from . import config


def get_repository_root():
    u'''
    リポジトリを展開するサーバ上のパスを取得
    '''

    return config.general.repository



def get_respository_by_project(proj):
    u'''
    プロジェクトからサーバ上のリポジトリパスを取得する
    '''

    root = get_repository_root()

    return os.path.join(root, str(proj.owner_id), str(proj.id))




    

    
