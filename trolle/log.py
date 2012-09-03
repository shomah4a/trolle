#-*- coding:utf-8 -*-
u'''
ログの共通フォーマット
'''

import logging


def mk_logger(name, level=logging.DEBUG):
    u'''
    ロガー作る
    '''

    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    logger.setLevel(level)

    fmt = '%(asctime)s %(levelname)s %(name)s:%(lineno)s pid=%(process)s tid=%(thread)s | %(message)s'
    handler.setFormatter(logging.Formatter(fmt))

    return logger
