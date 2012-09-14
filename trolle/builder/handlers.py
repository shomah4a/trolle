#-*- coding:utf-8 -*-
u'''
リポジトリパスから取ってくるためのもの
'''

import subprocess

from trolle import log

logger = log.mk_logger(__name__)


HANDLERS = {}


def _handler(f):

    HANDLERS[f.__name__.strip('_')] = f

    return f



def _exec(command):
    u'''
    コマンド実行
    '''
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)

    for line in p.stdout:
        logger.debug(line.rstrip())

    p.wait()

    return p.poll()



@_handler
def _git(repos, target):
    u'''
    git clone する
    '''

    return _exec(['git', 'clone', repos, target])


@_handler
def _mercurial(repos, target):
    u'''
    hg clone する
    '''

    return _exec(['hg', 'clone', repos, target])


@_handler
def _subversion(repos, target):
    u'''
    svn co する
    '''

    return _exec(['svn', 'co', repos, target])



def get_handler(typ):
    u'''
    ハンドラ取得
    '''

    if typ not in HANDLERS:
        raise ValueError(typ + 'is not supported')

    return HANDLERS[typ]
    
    
