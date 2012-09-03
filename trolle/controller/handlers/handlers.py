#-*- coding:utf-8 -*-

from tornado import ioloop, web, websocket


class AddSlashHandler(web.RequestHandler):
    u'''
    末尾に / をつけてリダイレクト
    '''

    def get(self, *args):

        self.redirect(self.request.uri+'/')
