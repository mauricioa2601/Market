import pymysql
class Conexion():
    def __init__(self):
        host='',
        username= '',
        password= '', #falta rellenar
        database= '' #falta rellenar
    
        self.db = pymysql.connect(host,username,password,database)
        self.cursor = self.db.cursor()    
    
    def ejecutarQuery(self,query):
        self.cursor.execute(query)
        self.commit
        return self.cursor
    
    def commit(self):
        self.db.commit
    def rollback(self):
        self.db.rollback
