from HelperFiles import mongo

"""
User Table:-
 - Passport_No (Primary Key)
 - Type
 - Country_Code
 - Given_Name
 - Surname
 - Sex
 - Nationality
 - Date_of_Birth
 - Place_of_Birth
 - Date_of_Issue
 - Date_of_Expiration
 - Issuing_Authority
"""

class User:
    # Method to create a new user
    def create_user(self, user_data):
        user_collection = mongo.db.users 
        user_collection.insert_one(user_data) 
    
    # Method to retrieve all users
    def get_user(self):
        user_collection = mongo.db.users
        user_data = user_collection.find({}, {'_id': 0}) #find({}, {'_id': 0}) -> {}: define extra criteria here, {'_id': 0}: exlude "_id" field
        return user_data
    
    # Method to get a lost of all existing Passport IDs
    def get_passport_ids(self):
        user_collection = mongo.db.users
        passport_ids = user_collection.distinct("Passport_No")
        return passport_ids