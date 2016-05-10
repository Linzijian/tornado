import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import MySQLdb
import torndb
from mysql import *
from managerFunc import *
from salesmanFunc import *

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html')
    def post(self):
        userid = self.get_argument('userid')
        password = self.get_argument('password')
        db = getMysqlConnection()
        sql1 = 'select * from USER_MANAGER where USER_ID=%d and USER_PASSWORD="%s" '%( int(userid), password )
        sql2 = 'select * from USER_SALESMAN where USER_ID=%d and USER_PASSWORD="%s" '%( int(userid), password )
        rs = db.query(sql1)
        if len(rs)>0:
            self.render('managerPage.html', userid=userid )
            return
        rs = db.query(sql2)
        if len(rs)>0:
            self.render('salesmanPage.html', userid=userid )
            return
        self.render('login.html')


class RegisterForManagerHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('registerForManager.html')
    def post(self):
        loginId = self.get_argument('loginId')
        name = self.get_argument('name')
        password = self.get_argument('password')
        sex = self.get_argument('sex')
        birthday = self.get_argument('birthday')
        nation = self.get_argument('nation')
        degree = self.get_argument('degree')
        telephone = self.get_argument('telephone')
        email = self.get_argument('email')
        qq = self.get_argument('qq')
        role = self.get_argument('role')
        field = self.get_argument('field')
        title = self.get_argument('title')
        flag = self.get_argument('flag')
        print loginId,name,password,sex,birthday,nation,degree,telephone,email,qq,role,field,title,flag
        sql = 'insert into USER_MANAGER ( USER_ID, USER_NAME, USER_PASSWORD, USER_SEX, USER_BIRTHDAY, USER_NATION, USER_DEGRESS, TELEPHONE_NUMBER, EMAIL_ADDRESS, USER_QQ, USER_ROLE, RESEARCH_FIELDS, USER_TITLE, FLAG_ROLE ) ' \
              'values( %d, "%s", "%s", "%s", "%s", "%s", "%s", %d, "%s", %d, "%s", "%s", "%s", "%s" )'%( int(loginId), name, password, sex, birthday, nation, degree, int(telephone), email, int(qq), role, field, title, flag )
        db = getMysqlConnection()
        db.execute(sql)
        self.render('login.html')

class RegisterForSalesmanHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('registerForSalesman.html')
    def post(self):
        loginId = self.get_argument('loginId')
        name = self.get_argument('name')
        password = self.get_argument('password')
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
        print loginId,name,password,sex,birthday,nation,degree,telephone,email,qq,role,field,mentor,flag
        sql = 'insert into USER_SALESMAN ( USER_ID, USER_NAME, USER_PASSWORD, USER_SEX, USER_BIRTHDAY, USER_NATION, USER_DEGRESS, TELEPHONE_NUMBER, EMAIL_ADDRESS, USER_QQ, USER_ROLE, RESEARCH_FIELDS, MENTORS, FLAG_ROLE ) ' \
              'values( %d, "%s", "%s", "%s", "%s", "%s", "%s", %d, "%s", %d, "%s", "%s", "%s", "%s" )'%( int(loginId), name, password, sex, birthday, nation, degree, int(telephone), email, int(qq), role, field, mentor, flag )
        db = getMysqlConnection()
        db.execute(sql)
        self.render('login.html')

class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        self.render('poem.html', roads=noun1, wood=noun2, made=verb,
                difference=noun3)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', LoginHandler),
                  (r'/login', LoginHandler),
                  (r'/registerForManager', RegisterForManagerHandler),
                  (r'/registerForSalesman', RegisterForSalesmanHandler),

                  (r'/managerInfoShow', ManagerInfoShowHandler),
                  (r'/managerInfoUpdate', ManagerInfoUpdateHandler),
                  (r'/managerPasswordUpdate', ManagerPasswordUpdateHandler),
                  (r'/querySalesman', QuerySalesmanHandler),

                  (r'/salesmanInfoShow', SalesmanInfoShowHandler),
                  (r'/salesmanInfoUpdate', SalesmanInfoUpdateHandler),
                  (r'/salesmanPasswordUpdate', SalesmanPasswordUpdateHandler),

                  (r'/poem', PoemPageHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()