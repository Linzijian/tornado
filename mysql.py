import MySQLdb
import torndb

class mysqlConfig:
    host = "127.0.0.1"
    port = "3306"
    database = "0509"
    user = "root"
    password = "8979319L"

def getMysqlConnection():
    db = torndb.Connection(mysqlConfig.host+":"+mysqlConfig.port, mysqlConfig.database, user=mysqlConfig.user, password=mysqlConfig.password)
    return db

