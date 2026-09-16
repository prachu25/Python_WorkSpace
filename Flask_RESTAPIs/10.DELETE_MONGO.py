from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Monogoconnectivity
client = MongoClient("CONNECTION_URL")
db = client['ecomprojectdb']
coll = db['prousers']


@app.route('/users/delete/<u_id>', methods = ['DELETE'])
def delete_user(u_id):

    result = coll.delete_one({"userid" : u_id})

    if result.deleted_count == 0:
        return jsonify({"error": "User Not FOund!"}), 404

    return jsonify({
        "msg": "user deleted successfully!"
    })

app.run(debug=True)