#-*- coding:utf-8 -*-

from trolle import utils


class File(object):
    u'''
    ファイル情報
    '''

    def __init__(self, fpath, tokens):

        self.filepath = fpath
        self.tokens = tokens


    def iter_tags(self):
        u'''
        タグだけ取り出す
        '''

        for token in self.tokens:

            if str(token.type).startswith('Token.Name'):
                yield token


    def iter_tokens(self):
        u'''
        トークン全部取り出す
        '''

        return iter(self.tokens)


    def register_file(self, sess):
        u'''
        ファイルとトークンを DB に登録する
        '''

        relpath = self.filepath[len(root):]



class Token(utils.SlotEqual):
    u'''
    トークン情報を持つ
    Pygments のトークンだけだと微妙に足りないので追加で情報を持たせる
    '''

    __slots__ = ['type', 'text', 'line', 'column']


    def __init__(self, type, text, line, column):

        self.type = type
        self.text = text
        self.line = line
        self.column = column



    def dump(self):
        u'''
        DB 登録用
        '''

        return dict(type=self.type,
                    identifier=self.text,
                    line=self.line,
                    column=self.column)



    @classmethod
    def mk_tokens(cls, tokens):
        u'''
        Pygments のトークンに対して変換処理
        '''

        column, line = 0, 0
        result = []


        for typ, text in tokens:

            tok = Token(typ, text, line, column)
            result.append(tok)

            column += len(text)

            if text == u'\n':
                line += 1
                column = 0

        return result


