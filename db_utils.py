import mysql.connector
import config
#punk_forum_db, username root, 127.0.0.1, port 3306


class DB:
    def __init__(self):

        db = mysql.connector.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            passwd=config.DB_PASSWD,
            database=config.DB_NAME
        )
        self.users = []
        self.users_name = []

    def add_user(self, hash):
        self.users.append(hash)

    def get_users(self):
        return self.users

    def add_name(self, name):
        self.users_name.append(name)

    def get_names(self):
        return self.users_name

    def user_info(self,name):
        return {"userinfo": 'info from database'}
