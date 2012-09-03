#-*- coding:utf-8 -*-

from tornado import ioloop, web, websocket

from . import utils
from .template import zpt
from .handlers import handlers, dblist

from trolle.model import tables


class TestHandler(web.RequestHandler):

    @utils.utf8html
    def get(self):

        return zpt.rendering('test', dict(handler=self))



def create_application():

    app = web.Application([
            ('/[^/]+', handlers.AddSlashHandler),
            ('/users/', dblist.DBListHandler, dict(table=tables.User,
                                                   search_func=tables.search_user,
                                                   create_func=tables.create_user)),
            ('/projects/', dblist.DBListHandler, dict(table=tables.Project,
                                                      search_func=tables.search_project,
                                                      create_func=tables.create_project)),
            ('/files/', dblist.DBListHandler, dict(table=tables.File,
                                                   search_func=tables.search_file,
                                                   create_func=tables.create_file)),
            ('/tags/', dblist.DBListHandler, dict(table=tables.Tag,
                                                  search_func=tables.search_tag,
                                                  create_func=tables.create_tag)),
            ('/comments/', dblist.DBListHandler, dict(table=tables.Comment,
                                                      search_func=tables.search_comment,
                                                      create_func=tables.create_comment)),
            ('/.*', TestHandler),
            ])

    return app

    
