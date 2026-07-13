from flask import Flask
from pymongo import MongoClient

app=Flask(__name__)

# MongoDB Connectivity
client=MongoClient("MONGO_CONNECTION_STRING")
db=client['spiderdb']
coll=db['films']

@app.route('/films', methods=['GET'])
def getallfilms():
    # Fetch all documents from the collection and store them as a list in the 'films' variable.
    films=list(coll.find({}, {"_id": 0}))
    return films



@app.route('/films/genre/<genre>', methods=['GET'])
def searchfilms(genre):
    print("Genre received:", genre)
    query = {'genre': genre}
    films = list(coll.find(query, {"_id": 0}))

    if len(films) == 0:
        return 'Not Found!'
    
    return films



@app.route('/films/year/<year>', methods=['GET'])
def searchOnYear(year):
    year=int(year)
    query={'releaseyr':year}
    films=list(coll.find(query))
    return films



if __name__ == '__main__':
    app.run(debug=True)



