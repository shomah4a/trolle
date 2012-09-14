#-*- coding:utf-8 -*-


from pygments import lexers

from . import token


def tokenize(filelike, fname):
    u'''
    ファイルっぽいオブジェクトからトークン生成
    '''

    lexer = lexers.get_lexer_for_filename(fname)

    text = filelike.read()
    tokens = lexer.get_tokens(text)

    tokens = token.Token.mk_tokens(tokens)

    return tokens






    
        
    

    

    
