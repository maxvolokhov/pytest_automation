from pymongo import MongoClient


class BaseMongo:
    def __init__(self, host, port, db_name):
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]

    def insert_one(self, collection_name, data):
        collection = self.db[collection_name]
        return collection.insert_one(data)

    def insert_many(self, collection_name, data_list):
        collection = self.db[collection_name]
        return collection.insert_many(data_list)

    def find_one(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.find_one(query)

    def find(self, collection_name, query):
        collection = self.db[collection_name]
        return list(collection.find(query))

    def update_one(self, collection_name, query, update_data):
        collection = self.db[collection_name]
        return collection.update_one(query, {'$set': update_data})

    def update_many(self, collection_name, query, update_data):
        collection = self.db[collection_name]
        return collection.update_many(query, {'$set': update_data})

    def delete_one(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.delete_one(query)

    def delete_many(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.delete_many(query)

    def close(self):
        self.client.close()
