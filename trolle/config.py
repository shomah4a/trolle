#-*- coding:utf-8 -*-
u'''
設定とか置いておく場所
'''

import os
import ConfigParser as configparser

from . import log


logger = log.mk_logger(__name__)


class ConfigureError(NameError):
    u'''
    設定トチったときに出るエラー
    '''


class Section(object):
    u'''
    セクションごとの設定情報を持っておくためのクラス
    params と defaults で指定したパラメータ名以外を使うと例外を投げる
    converters でセクションごとに変換を掛けたりできる

    :param converters: パラメータ変換を行う場合の変換関数
    :type converters: dict<str, `ParamConverter`_)
    :param params: パラメータ名のリスト(default: None)
    :type params: [str]
    :param defaults: パラメータ名とデフォルト値の辞書
    :type defaults: dict<str, object>
    '''

    def __init__(self, params=[], defaults={}, converters={}):

        self.__dict__['__keys'] = set(defaults.keys() + params)
        self.__converters = converters
        self.__dict__.update(dict((x, None) for x in params))
        self.__dict__.update(defaults)


    def __setattr__(self, key, value):

        if key.startswith('_' + self.__class__.__name__ + '__'):
            super(Section, self).__setattr__(key, value)
            return

        if key not in self.__dict__['__keys']:
            msg = 'Invalid config param: %s' % key
            raise ConfigureError(msg)

        value = value.strip()

        if key in self.__converters:
            value = self.__converters[key](value)

        super(Section, self).__setattr__(key, value)


root = '.'

# 色々
general = Section(
    converters=dict(repository=os.path.expandvars),
    defaults=dict(repository='/tmp/path'))

# サーバの設定
server = Section(
    converters=dict(port=int),
    defaults=dict(port=8080))


# DB 設定
db = Section(
    converters=dict(echo=int),
    defaults=dict(
        echo=1,
        uri='mysql+pymysql://root@localhost/trolle_test'))



def load_file(root_dir, fpath):
    u'''
    設定ファイルをひとつ読み込む
    '''

    g = globals()

    if not os.path.exists(fpath):
        raise OSError('Config file not found: ' + fpath)

    parser = configparser.SafeConfigParser()
    parser.read(fpath)

    for section in  parser.sections():

        s = g.get(section)

        if s is None or not isinstance(g[section], Section):
            raise ConfigureError('Invalid section: ' + section)

        options = parser.options(section)

        for option in options:
            value = parser.get(section, option)
            setattr(s, option, value)
            logger.info('Optiopn: [%s] %s = %s' % (section, option, getattr(s, option)))



def init_config(root_dir, fpathes):
    u'''
    設定ファイルを読み込む
    '''

    global root

    root = root_dir

    for fpath in fpathes:

        load_file(root_dir, fpath)

    __init_zcml()


def __init_zcml():

    from zope.configuration import xmlconfig

    zcml = os.path.join(os.path.dirname(__file__), 'configure.zcml')

    xmlconfig.file(zcml)



