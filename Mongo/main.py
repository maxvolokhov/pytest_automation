from Mongo.base_mongo import BaseMongo
from Mongo.product_collection import ProductCollection
from Mongo.user_collection import UserCollection

if __name__ == "__main__":
    mongo_client = BaseMongo('localhost', 27017, 'mydb')

    user_collection = UserCollection('localhost', 27017, 'mydb')
    product_collection = ProductCollection('localhost', 27017, 'mydb')

    user_data = {'name': 'John', 'email': 'john@example.com'}
    user_collection.insert_one('users', user_data)

    found_user = user_collection.find_user_by_name('John')
    print("Found User:", found_user)

    update_data = {'email': 'new_email@example.com'}
    user_collection.update_user('John', update_data)
    updated_user = user_collection.find_user_by_name('John')
    print("Updated User:", updated_user)

    product_data_list = [
        {'name': 'Product 1', 'price': 10.99},
        {'name': 'Product 2', 'price': 19.99},
    ]
    product_collection.insert_many('products', product_data_list)

    all_products = product_collection.find('products', {})
    print("All Products:", all_products)

    product_collection.delete_one('products', {'name': 'Product 1'})
    remaining_products = product_collection.find('products', {})
    print("Remaining Products:", remaining_products)

    mongo_client.close()
