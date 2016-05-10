import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import MySQLdb
import torndb
from mysql import *

class SalesmanInfoShowHandler(tornado.web.RequestHandler):
    def get(self):
        userid = self.get_argument('userid')
        db = getMysqlConnection()
        sql = 'select * from USER_SALESMAN where USER_ID = %d'%(int(userid))
        rs = db.get(sql)
        # print rs
        self.render("salesmanInfoShow.html", userid= userid, rs = rs )

class SalesmanInfoUpdateHandler(tornado.web.RequestHandler):
    def get(self):
        userid = self.get_argument('userid')
        db = getMysqlConnection()
        sql = 'select * from USER_SALESMAN where USER_ID = %d'%(int(userid))
        rs = db.get(sql)
        self.render("salesmanInfoUpdate.html", userid= userid, rs = rs )
    def post(self):
        loginId = self.get_argument('loginId')
        name = self.get_argument('name')
        sex = self.get_argument('sex')
        birthday = self.get_argument('birthday')
        nation = self.get_argument('nation')
        degree = self.get_argument('degree')
        telephone = self.get_argument('telephone')
        email = self.get_argument('email')
        qq = self.get_argument('qq')
        role = self.get_argument('role')
        field = self.get_argument('field')
        mentor = self.get_argument('mentor')
        flag = self.get_argument('flag')
        db = getMysqlConnection()
        sql = 'update USER_SALESMAN set USER_ID=%d, USER_NAME="%s", USER_SEX="%s", USER_BIRTHDAY="%s", USER_NATION="%s", ' \
              'USER_DEGRESS="%s", TELEPHONE_NUMBER=%d, EMAIL_ADDRESS="%s", USER_QQ=%d, RESEARCH_FIELDS="%s"' \
              ' , MENTORS="%s" where USER_ID = %d  '\
              %( int(loginId), name, sex, birthday, nation, degree, int(telephone), email, int(qq), field, mentor, int(loginId))
        db.execute(sql)
        sql = 'select * from USER_SALESMAN where USER_ID = %d'%(int(loginId))
        rs = db.get(sql)
        self.render("salesmanInfoUpdate.html", userid= loginId, rs = rs )

class SalesmanPasswordUpdateHandler(tornado.web.RequestHandler):
    def get(self):
        userid = self.get_argument('userid')
        db = getMysqlConnection()
        sql = 'select * from USER_SALESMAN where USER_ID = %d'%(int(userid))
        rs = db.get(sql)
        self.render("salesmanPasswordUpdate.html", userid= userid, rs = rs )
    def post(self):
        userid = self.get_argument('userid')
        password = self.get_argument('password')
        db = getMysqlConnection()
        sql = 'update USER_SALESMAN set USER_PASSWORD="%s" where USER_ID = %d  '\
              %( password, int(userid))
        db.execute(sql)
        sql = 'select * from USER_SALESMAN where USER_ID = %d'%(int(userid))
        rs = db.get(sql)
        self.render("salesmanPasswordUpdate.html", userid= userid, rs = rs )








