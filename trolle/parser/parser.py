#-*- coding:utf-8 -*-


from pygments import lexers, util

from . import token


def is_parsable(filename):
    u'''
    ファイル名からパースできるかどうかをチェック
    :param str filename: ファイル名
    :return: パース可能かどうか
    :rtype: bool
    '''

    try:
        lexer = lexers.get_lexer_for_filename(filename)
        return True
    except util.ClassNotFound:
        return False



def tokenize(filelike, fname):
    u'''
    ファイルっぽいオブジェクトからトークン生成

    :param filelike filelike: ファイルオブジェクトみたいなやつ
    :param basestring fname: 文字列
    :return: トークン列
    :rtype: list< `Token <trolle.token.Token>`_ >
    '''

    lexer = lexers.get_lexer_for_filename(fname)

    text = filelike.read()
    tokens = lexer.get_tokens(text)

    tokens = token.Token.mk_tokens(tokens)

    return tokens


