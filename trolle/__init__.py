#-*- coding:utf-8 -*-
u'''
みんなでソース読むツール trolle
'''
__import__('pkg_resources').declare_namespace(__name__)

__version__ = '0.1.0'
__license__ = 'GPLv2'
__author__ = '@shomah4a'


import argparse

from . import config


def parse_args(args):
    u'''
    コマンドラインパーサってやつ
    '''

    parser = argparse.ArgumentParser(description=u'とろーるさんだよー')
    
    parser.add_argument('--root', dest='root', default='.')
    parser.add_argument('--conf', dest='conf', action='append', default=[])

    return parser.parse_args(args)



def serve(conf):

    from tornado import ioloop, web, websocket

    from .controller import application

    app = application.create_application()
    app.listen(conf.port)
    ioloop.IOLoop.instance().start()


def monkey():

    from zope import i18n

    i18n.translate = None

    
def main(args):
    u'''
    エントリポイントというもの
    '''

    from .model import session
    
    parsed = parse_args(args)

    config.init_config(parsed.root, parsed.conf)

    session.initialize(config.db)

    monkey()

    serve(config.server)


if __name__ == '__main__':

    import sys

    main(sys.argv[1:])

