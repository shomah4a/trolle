#-*- coding:utf-8 -*-


from pygments import lexers

from . import token


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


