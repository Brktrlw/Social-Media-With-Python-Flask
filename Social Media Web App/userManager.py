
import sqlite3
from fileLogger import FileErrorLogger
from colored import fg, bg, attr
from BaseDataBaseManager import DataBaseManager
class UserManager():
    @staticmethod # Kullanıcı bilgilerini kullanıcı adı ile aldığımız method
    def getUserDataByUserNickName(userNickname):
        try:
            connection = sqlite3.connect("Database.db")
            connection.row_factory=DataBaseManager.dict_factory
            cursor = connection.cursor()
            cursor.execute(f"Select * from Users where UserNickName='{userNickname}'")
            userData=cursor.fetchall()
            return userData
        except Exception as e:
            FileErrorLogger.FileLogger(e)
            print(f'%s%s {e} !!! %s' % (fg('white'), bg('red'), attr('reset')))
    @staticmethod
    def isLogin(userNickName,userPassword):
        try:
            connection = sqlite3.connect("Database.db")
            #connection.row_factory=DataBaseManager.dict_factory
            cursor = connection.cursor()
            cursor.execute(f"Select * from Users where usernickname='{userNickName}' and userpassword='{userPassword}'")
            isLogin=cursor.fetchall()
            return isLogin
        except Exception as e:
            FileErrorLogger.FileLogger(e)
            print(f'%s%s {e} !!! %s' % (fg('white'), bg('red'), attr('reset')))

    @staticmethod
    def getUserIdByUserNickName(userNickName):
        try:
            connection = sqlite3.connect("Database.db")
            cursor = connection.cursor()
            cursor.execute(f"Select UserId from Users where usernickname='{userNickName}'")
            userId=cursor.fetchall()
            return userId
        except Exception as e:
            FileErrorLogger.FileLogger(e)
            print(f'%s%s {e} !!! %s' % (fg('white'), bg('red'), attr('reset')))


    ######
    @staticmethod
    def isUserLoginDataTrue():
        try:
            connection=sqlite3.connect("Database.db")
            cursor=connection.cursor()
            cursor.execute("")
            isUserLoginDataTrue=cursor.fetchall()
        except Exception as e:
            FileErrorLogger.FileLogger(e)
            print(f'%s%s {e} !!! %s' % (fg('white'), bg('red'), attr('reset')))
        finally:
            connection.close()
    ######



