import sqlite3
from fileLogger import FileErrorLogger
from colored import fg, bg, attr


class FriendsManager():
    @staticmethod
    def isFriendByUserId(user1Id,user2Id):
        try:
            connection = sqlite3.connect("Database.db")
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM Friends where UserId1={user1Id} and UserId2={user2Id} or UserId1={user2Id} and userId2={user1Id}")
            isFriend=cursor.fetchall()
            return isFriend
        except Exception as e:
            FileErrorLogger.FileLogger(e)
            print(f'%s%s {e} !!! %s' % (fg('white'), bg('red'), attr('reset')))
        finally:
            connection.close()

    @staticmethod
    def getFriendRequestByUsersId(senderUserId,receiverUserId):
        try:
            connection = sqlite3.connect("Database.db")
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM FriendsRequest where ReceiverUserId='{receiverUserId}' and SenderUserId='{senderUserId}'")
            isSendRequestFriend=cursor.fetchall()
            return isSendRequestFriend
        except Exception as e:
            FileErrorLogger.FileLogger(e)
            print(f'%s%s {e} !!! %s' % (fg('white'), bg('red'), attr('reset')))
        finally:
            connection.close()

    @staticmethod
    def getFriendsByUserName():
        try:
            connection = sqlite3.connect("Database.db")
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM Friends where userId1")
            isSendRequestFriend=cursor.fetchall()
            return isSendRequestFriend
        except Exception as e:
            FileErrorLogger.FileLogger(e)
            print(f'%s%s {e} !!! %s' % (fg('white'), bg('red'), attr('reset')))
        finally:
            connection.close()

    @staticmethod #arkadaşlık isteği göndermeye yarayan method
    def addRequestFriendByUsersId(senderUserId,receiverUserId):
        try:
            connection = sqlite3.connect("Database.db")
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO FriendsRequest ('ReceiverUserId','SenderUserId') VALUES ('{receiverUserId}','{senderUserId}')")
            connection.commit()
        except Exception as e:
            FileErrorLogger.FileLogger(e)
            print(f'%s%s {e} !!! %s' % (fg('white'), bg('red'), attr('reset')))
        finally:
            connection.close()

    @staticmethod
    def deleteRequestFriendByUsersId(senderUserId,receiverUserId):
        try:
            connection = sqlite3.connect("Database.db")
            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM FriendsRequest where ReceiverUserId={receiverUserId} and SenderUserId={senderUserId}")
            connection.commit()
        except Exception as e:
            FileErrorLogger.FileLogger(e)
            print(f'%s%s {e} !!! %s' % (fg('white'), bg('red'), attr('reset')))
        finally:
            connection.close()
