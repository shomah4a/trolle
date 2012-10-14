#-*- coding:utf-8 -*-

import sqlalchemy as al
from sqlalchemy import sql
from sqlalchemy.ext import declarative as decl


Base = decl.declarative_base()


class User(Base):
    u'''
    ユーザテーブルの定義

    :param int id: ユーザ ID (PK)
    :param str name: ユーザ名
    '''

    __tablename__ = 'users'
    __table_args__ = (
        {'mysql_engine': 'InnoDB'})

    id = decl.Column(al.Integer, primary_key=True, autoincrement=True)
    name = decl.Column(al.Unicode(255), nullable=False)



class LoginInfo(Base):
    u'''
    ログインするための情報

    :param int user_id: ユーザ ID (PK, FK)
    :param str service_name: サービス名(twitter とか facebook とか) (PK)
    :param str service_user_id: サービス上のユーザ ID
    '''

    __tablename__ = 'login_infos'
    __table_args__ = (
        {'mysql_engine': 'InnoDB'})

    user_id = decl.Column(al.Integer, al.ForeignKey('users.id'), primary_key=True)
    service_name = decl.Column(al.Unicode(255), primary_key=True)
    service_user_id = decl.Column(al.Unicode(255), nullable=False)



class Project(Base):
    u'''
    ソースコード閲覧のプロジェクト定義

    :param int id: プロジェクト ID (PK)
    :param int owner_id: プロジェクトのオーナー (FK)
    :param str project_name: プロジェクト名
    :param str repository_uri: リポジトリのパス
    :param str repository_type: リポジトリの形式 (git とか mercurial とか)
    :param str encoding: リポジトリのエンコード設定 (default: utf-8)
    :param bool ready: プロジェクトのセットアップが終わったかどうか
    '''

    __tablename__ = 'projects'
    __table_args__ = (
        {'mysql_engine': 'InnoDB'})

    id = decl.Column(al.Integer, primary_key=True, autoincrement=True)
    owner_id = decl.Column(al.Integer, al.ForeignKey('users.id'), nullable=False)
    name = decl.Column(al.Unicode(255), nullable=False)
    repository_uri = decl.Column(al.UnicodeText(65535), nullable=False)
    repository_type = decl.Column(al.Unicode(255), nullable=False)
    encoding = decl.Column(al.Unicode(255), default=u'utf-8', nullable=False)
    ready = decl.Column(al.Boolean, default=False, nullable=False)



class File(Base):
    u'''
    プロジェクトに含まれるファイルのパス
    blob 入れるかどうかは要検討

    :param int id: ファイルの ID
    :param int project_id: プロジェクト ID (PK, FK)
    :param str filepath: ファイルパス (PK)
    '''

    __tablename__ = 'files'
    __table_args__ = (
        al.UniqueConstraint('project_id', 'filepath', name='uc_file'),
        {'mysql_engine': 'InnoDB'})

    id = decl.Column(al.Integer, autoincrement=True, primary_key=True)
    project_id = decl.Column(al.Integer, al.ForeignKey('projects.id'), nullable=False)
    filepath = decl.Column(al.Unicode(255), nullable=False)



class Tag(Base):
    u'''
    ソースコードのタグ付け情報

    :param int id: タグ ID (PK)
    :param int file_id: ファイルの ID (FK)
    :param str identifier: タグの識別子
    :param int line: タグの行
    :param int column: 行内の開始位置
    :param int type: タグのタイプ(定義か参照か)

    '''

    __tablename__ = 'tags'
    __table_args__ = (
        al.UniqueConstraint('file_id', 'identifier', 'line',
                            'column', 'type', name='uc_tag'),
        {'mysql_engine': 'InnoDB'})

    id = decl.Column(al.Integer, primary_key=True, autoincrement=True)
    file_id = decl.Column(al.Integer, al.ForeignKey('files.id'), nullable=False)
    identifier = decl.Column(al.Unicode(255), nullable=False)
    line = decl.Column(al.Integer, nullable=False)
    column = decl.Column(al.Integer, nullable=False)
    type = decl.Column(al.Unicode(255), nullable=False)



class Comment(Base):
    u'''
    ソースコードのコメント

    :param int id: コメント ID
    :param int user_id: ユーザ ID (FK)
    :param int file_id: ファイル ID (FK)
    :param int line: 行番号
    :param str text: コメント内容

    '''

    __tablename__ = 'comments'
    __table_args__ = (
        al.UniqueConstraint('user_id', 'file_id', 'line'),
        {'mysql_engine': 'InnoDB'})

    id = decl.Column(al.Integer, primary_key=True, autoincrement=True)
    user_id = decl.Column(al.Integer, al.ForeignKey('users.id'), nullable=False)
    file_id = decl.Column(al.Integer, al.ForeignKey('files.id'), nullable=False)
    line = decl.Column(al.Integer, nullable=False)
    text = decl.Column(al.UnicodeText(65535), nullable=False)



def _create_maker(cls):
    u'''
    作るための関数を作る
    '''

    def create_entry(sess, **kw):

        entry = cls(**kw)
        sess.add(entry)

        return entry

    return create_entry


def _search_maker(cls):
    u'''
    検索のための関数を作る
    '''

    def search_entry(sess, **kw):

        tbl = cls.__table__

        keys = tbl.c.keys()
        cols = [tbl.c[x] for x in keys]
        d = dict(zip(keys, cols))

        query = sql.select(cols,
                           sql.and_(*[d[k] == v for k, v in kw.items()]),
                           tbl).order_by(tbl.c.id)

        result_proxy = sess.execute(query)

        results = list(result_proxy)

        return [cls(**dict(zip(keys, result)))
                for result in results]

    return search_entry


create_user = _create_maker(User)
search_user = _search_maker(User)

create_login_info = _create_maker(LoginInfo)
search_login_info = _search_maker(LoginInfo)

create_project = _create_maker(Project)
search_project = _search_maker(Project)

create_file = _create_maker(File)
search_file = _search_maker(File)

create_tag = _create_maker(Tag)
search_tag = _search_maker(Tag)

create_comment = _create_maker(Comment)
search_comment = _search_maker(Comment)

