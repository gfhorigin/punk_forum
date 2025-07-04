class DB:
    def __init__(self):
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
