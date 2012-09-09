#-*- coding:utf-8 -*-



class File(object):
    u'''
    ファイル情報
    '''


    def __init__(self, fpath, tokens):

        self.fpath = fpath
        self.tokens = tokens


    def list_tags(self):

        for token in self.tokens:

            if str(token.type).startswith('Token.Name'):
                yield token



class Token(object):
    u'''
    トークン情報を持つ
    Pygments のトークンだけだと微妙に足りないので追加で情報を持たせる
    '''

    __slots__ = ['type', 'text', 'column', 'index']
    
    
    def __init__(self, type, text, line, column):

        self.type = type
        self.text = text
        self.line = line
        self.column = column


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

