from flask import Flask,request,jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
import re

app1 = Flask(__name__)


client = MongoClient("mongodb://localhost:27017")
db = client["user"]
collection = db["data"]

@app1.route('/addproduct' ,methods=['POST'])
def addproduct():
    data = request.json
    email = data.get("useremail")
    mobile = data.get("usermobile")

   
        

    if collection.find_one({'useremail':email}):
        return("Insertion acknowledged")
    if collection.find_one({'usermobile':mobile}):
        return("acknowledged")
    if data:
        result = collection.insert_one(data)
        return jsonify({'_id':str(result.inserted_id)})
    else:
        return jsonify({"invalid data"})
    



@app1.route('/getproduct' ,methods=['GET'])
def getproduct():
    user = request.json
    name = user.get("username")
    if collection.find_one({'username':name}):
        return('log in success')
    if user:
        result = collection.find_one(user)
        return jsonify({'_id':str(result)})

    else:
        return jsonify({'invalide data'})




@app1.route('/detail', methods=['POST'])
def detail():
    data = request.json
    email = data.get("email")
    mobile = data.get("mobile")
    password = data.get("password")

    # Email validation
    email_regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    if not re.match(email_regex, email):
        return jsonify({"error": "Invalid email address."}), 

    mobile_regex = r'^\d{10}$'
    if not re.match(mobile_regex, mobile):
        return jsonify({"error": "Invalid phone number. It must be 10 digits."}), 

    
    if len(password) < 8:
        return jsonify({"error": "Password must be at least 8 characters long."}), 
    if not re.search(r"[A-Z]", password):
        return jsonify({"error": "Password must contain at least one uppercase letter."}), 
    if not re.search(r"[a-z]", password):
        return jsonify({"error": "Password must contain at least one lowercase letter."}), 
    if not re.search(r"\d", password):
        return jsonify({"error": "Password must contain at least one digit."}), 
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return jsonify({"error": "Password must contain at least one special character."}), 

    
    if collection.find_one({"email": email}):
        return jsonify({"message": "Email is already registered"}), 


    if collection.find_one({"phone no": mobile}):
        return jsonify({"message": "Phone number is already registered"}), 


    if data:
        result = collection.insert_one(data)
        return jsonify({"_id": str(result.inserted_id)}), 
    else:
        return jsonify({"error": "Invalid data"}), 



    
if __name__ == "__main__":
    app1.run(debug=True)