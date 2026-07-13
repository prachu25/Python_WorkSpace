from flask import Flask , request, jsonify
from pymongo import MongoClient

app=Flask(__name__)

# MongoDB Connectivity
client=MongoClient("MONGO_CONNECTION_STRING_")
db=client['spiderdb']
coll=db['students']


@app.route('/student/add', methods=['POST'])
def add_student():
    data=request.get_json()
    result=coll.insert_one(data)
    return jsonify({
        'message':'new student added',
        'id':str(result.inserted_id)
    })

app.run(debug=True)
                   