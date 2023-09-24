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
 - Travel_History
   [
     - Airport
     - Date
     - Time
   ]
 - Face
"""

class User:
    # Method to create a new user
    def create_user(self, user_data):
        user_collection = mongo.db.users 
        user_collection.insert_one(user_data) 
    
    # Method to retrieve all users
    def get_user(self, user_id):
        user_collection = mongo.db.users
        query = {} 
    
        # If user_id is provided, add it to the query
        if user_id:
            query['Passport_No'] = user_id

        user_data = user_collection.find(query, {'_id': 0, "Travel_History": 0})
        return list(user_data)
    
    # Method to get a list of all existing Passport IDs
    def get_passport_ids(self):
        user_collection = mongo.db.users
        passport_ids = user_collection.distinct("Passport_No")
        return passport_ids
    
    # Method to add travel details for a User
    def update_travel_history(self, passport_no, travel_entry):
        user_collection = mongo.db.users
        query = {"Passport_No": passport_no}

        # Update the user's travel history using the $push operator
        update_query = {"$push": {"Travel_History": travel_entry}}

        user_collection.update_one(query, update_query)

    # Method to retrieve Travel History of a User
    def get_travel_history(self, user_id):
        user_collection = mongo.db.users
        user_data = user_collection.find({"Passport_No" : user_id}, {"Travel_History": 1, '_id': 0})
        user_data = list(user_data)

        # If user not found
        if(user_data == []):
            return []
        
        # Parsing the data in a suitable format
        return user_data[0]["Travel_History"]