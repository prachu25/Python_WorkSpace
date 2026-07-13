from flask import Flask, request, jsonify
from pymongo import MongoClient

app=Flask(__name__)

# MongoDB COnnnectivity
client=MongoClient("MONGO_CONNECTION_STRING_")
db=client['spiderdb']
coll=db['mobilesales']

@app.route('/users/modify/<id>' , methods=['PUT'])
def update_mobile(id):
    data=request.get_json()

    if not data:
        return jsonify({'error': "NO Data received"}) , 400
    

    result = coll.update_one(
        {"_id": int(id)},
        {"$set": data}
    )


    if result.matched_count==0:
        return jsonify({'error': 'User not Found! '}), 404
    

    return jsonify({
        "message":"User Data Modified Successfully",
        "_id":id
    })


app.run(debug=True)
