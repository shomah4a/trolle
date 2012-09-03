#-*- coding:utf-8 -*-

import functools


def set_content_type(f, mime, charset=None):
    u'''
    指定した mimetype に設定する
    '''

    @functools.wraps(f)
    def call(self, *args, **argd):

        ct = mime

        if charset is not None:
            ct += ';charset=' + charset

            self.set_header('Content-Type', ct)

        result = f(self, *args, **argd)

        self.write(result.encode('utf-8'))

    return call
    


def utf8html(f):
    u'''
    Content-Type を text/html;charset=utf-8 であると仮定して設定する
    '''

    return set_content_type(f, 'text/html', 'utf-8')


def utf8text(f):
    u'''
    Content-Type を text/plain;charset=utf-8 であると仮定して設定する
    '''

    return set_content_type(f, 'text/plain', 'utf-8')



def get_first_params(d):
    u'''
    パラメータのひとつ目を取ってくる
    '''

    return dict((k, v[0]) for k, v in d.iteritems())

