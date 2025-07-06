import mysql.connector
import os
from dotenv import load_dotenv
#punk_forum_db, username root, 127.0.0.1, port 3306
class DB:
    def __init__(self):
        load_dotenv()

        db = mysql.connector.connect(
            host="mysql",
            user="root",
            passwd=os.getenv('DB_PASSWD'),
            database="punk_forum_db"
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
