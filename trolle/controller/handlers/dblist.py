#-*- coding:utf-8 -*-

from tornado import web

from trolle.controller import utils
from trolle.model import session
from trolle.controller.template import zpt


class DBListHandler(web.RequestHandler):
    u'''
    DB からリストする
    '''

    def __init__(self, app, request, table, search_func, create_func):

        super(DBListHandler, self).__init__(app, request)
        
        self.table = table
        self.search = search_func
        self.create = create_func



    @utils.utf8html
    def get(self):
        u'''
        一覧
        '''

        with session.Session() as sess:
        
            results = self.search(sess,
                                  **utils.get_first_params(self.request.arguments))

        return zpt.rendering('list', dict(handler=self,
                                          request=self.request,
                                          results=results,
                                          table=self.table))

    def post(self):
        u'''
        追加
        '''

        keys = [x for x in self.table.__table__.c.keys()
                if x != 'id']
        
        params = dict((key, self.get_argument(key))
                      for key in keys)

        with session.Session() as sess:
            with sess.begin():
                self.create(sess, **params)

        self.redirect(self.request.uri)

