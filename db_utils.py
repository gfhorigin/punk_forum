import mysql.connector
import config
import datetime
import re


class DB:
    def __init__(self):
        self.db = mysql.connector.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            passwd=config.DB_PASSWD,
            database=config.DB_NAME,
            port=config.DB_PORT
        )
        self.cursor = self.db.cursor(buffered=True)

    def add_user(self, login_hash, email, nickname, unique_name):
        current_time = str(datetime.datetime.now())

        self.cursor.execute(f'INSERT INTO {config.TABLE_USERS} '
                            f'(unique_name, nickname,email, login_hash, last_login, created_at, updated_at )'
                            f'VALUES(%s, %s, %s, %s, %s, %s,%s)',
                            (unique_name, nickname, email, login_hash, current_time, current_time, current_time))

        self.db.commit()

    def get_users(self):
        return self.users

    def get_emails(self):  # ------------возможно в будущем удалить
        self.cursor.execute(f'SELECT email FROM {config.TABLE_USERS}')
        return self.cursor.fetchall()

    def user_info(self, name):
        return {"userinfo": 'info from database'}

    def get_unique(self):  # ------------возможно в будущем удалить
        self.cursor.execute(f'SELECT unique_name FROM {config.TABLE_USERS}')
        return self.cursor.fetchall()

    def email_exists(self, email):
        self.cursor.execute(f'SELECT email FROM {config.TABLE_USERS} WHERE email = %s', (email,))
        if self.cursor.fetchone():
            return True
        return False

    def unique_exists(self, unique):
        self.cursor.execute(f'SELECT unique_name FROM {config.TABLE_USERS} WHERE unique_name = %s', (unique,))
        if self.cursor.fetchone():
            return True
        return False

    def hash_check(self, login_hash):

        self.cursor.execute(f'SELECT login_hash FROM {config.TABLE_USERS} WHERE login_hash = %s', (login_hash,))
        if self.cursor.fetchone() :
            return True
        return False

    def get_user_auth_info_by_email(self, email):
        self.cursor.execute(f'SELECT unique_name, nickname, email, id  FROM {config.TABLE_USERS} WHERE email = %s',
                            (email,))
        data = self.cursor.fetchone()
        return {
            "unique_name": data[0],
            "nickname": data[1],
            "email": data[2],
            "id": data[3]
        }

    def delete_user(self, email): # --------------только для тестов
        self.cursor.execute(f'DELETE FROM {config.TABLE_USERS} WHERE email = %s', (email,))
        self.db.commit()

