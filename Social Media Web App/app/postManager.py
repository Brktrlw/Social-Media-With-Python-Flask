import sqlite3
from fileLogger import FileErrorLogger
from colored import fg, bg, attr

class PostManager():
    @staticmethod
    def addPost():
        try:
            connection = sqlite3.connect("Database.db")
            cursor = connection.cursor()
            #cursor.execute(f"INSERT INTO Posts (PostTitle,PostDescription,PostLike,PostDate,CategorieId) VALUES ('{}','{}','{}','{}','{}','{}','')")
            connection.commit()
        except Exception as e:
            FileErrorLogger.FileLogger(e)
            print(f'%s%s {e} !!! %s' % (fg('white'), bg('red'), attr('reset')))
        finally:
            connection.close()