from base_mongo import BaseMongo


class UserCollection(BaseMongo):
    def __init__(self, host, port, db_name):
        super().__init__(host, port, db_name)

    def find_user_by_name(self, name):
        query = {'name': name}
        return self.find_one('users', query)

    def update_user(self, name, new_data):
        query = {'name': name}
        return self.update_one('users', query, new_data)

    def delete_user(self, name):
        query = {'name': name}
        return self.delete_one('users', query)
