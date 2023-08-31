from HelperFiles import mongo

class User:
    def add_user(self, user_data):
        user_collection = mongo.db.users
        user_collection.insert_one(user_data)
    
    def get_users(self):
        user_collection = mongo.db.users
        users = user_collection.find({}, {'_id': 0})
        return users