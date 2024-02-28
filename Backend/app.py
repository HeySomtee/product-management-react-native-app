from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson import ObjectId



app = Flask(__name__)
CORS(app)

mongo_uri = "mongodb+srv://sportee_admin:tkcx6qyh7m@cluster0.opksht3.mongodb.net/Project_db?retryWrites=true&w=majority"
client = MongoClient(mongo_uri) 

database_name = "Project_db"
db = client[database_name]

collection_name = "ilog_db"
collection = db[collection_name]


@app.route('/test', methods=['GET', 'POST'])
def test_route():
    text = 'Hello World'
    return text

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user_email = request.json.get('email')
        password = request.json.get('password')

        existing_user = collection.find_one({'useremail': user_email})
        if existing_user:
            response_message = {'res': 'Email already exists'}
            response = jsonify(response_message)
            print(response.data) 
            return response.data, 222

        #TODO hash/salt password
        hashed_password = password  # generate_password_hash(password, method='sha256')
        user_data = {'useremail': user_email, 'password': hashed_password}
        collection.insert_one(user_data)
        response_message = {'res': 'User registered successfully'}
        response = jsonify(response_message)
        print(response.data) 
        return response.data, 223
    pass    
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_email = request.json.get('email')
        password = request.json.get('password')
        
        existing_user = collection.find_one({'useremail': user_email, 'password': password})
        if existing_user:
            print(access_token)
            response_message = {'res': 'User login successful', 'access_token': access_token}
            response = jsonify(response_message)
            print(response.data) 
            return response.data, 223
        else:
            response_message = {'res': 'invalid email or password'}
            response = jsonify(response_message)
            return response, 222
    pass        
                                                                
                                                                                           
if __name__ == '__main__':
    app.run(debug=True)
