


from flask import Flask,request,jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)


client = MongoClient("mongodb://localhost:27017")
db = client["product"]
collection = db["item"]

@app.route('/addproduct' ,methods=['POST'])
def approduct():
    data = request.json
    result = collection.insert_one(data)
    return jsonify({'_id':str(result.inserted_id)})




@app.route('/getproduct' ,methods=['GET'])
def getproduct():
   result = list(collection.find())
   for res in result:
    res['_id'] = str(res['_id'])
   return jsonify(result)
   
   
  

@app.route("/updateproduct/<_id>" ,methods=["PUT"])
def updateproduct(_id):
  data = request.json
  object_id = ObjectId(_id)
  result = collection.update_one({'_id': object_id}, {'$set': data})
  return jsonify({"MESSAGE": "PRODUCT UPDATE"})
# return jsonify({'_id':str(result)})



@app.route("/deleteproduct/<_id>" ,methods=["DELETE"])
def deleteproduct(_id):
   data = request.json 
   object_id = ObjectId(_id)
   result = collection.delete_one({'_id': object_id})
   return jsonify({'_id':str(result)})



@app.route("/getname/<_id>" ,methods=["GET"])
def getname(_id):
   object_id = ObjectId(_id)
   result = collection.find_one({'_id': object_id})
   result['_id'] =str(result['_id'])
   return jsonify(result)
 



if __name__ == "__main__":
   app.run(debug=True)




