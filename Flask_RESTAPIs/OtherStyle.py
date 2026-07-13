from flask import Flask

app=Flask(__name__)

@app.route('/player',methods=['GET'])
def get_player():
    p={
        "name":"Raju",
        "age":23,
        "gender":"Male",
        "club":"liverpool",
        "position":"midfilder"
    }

    return p



# @app.route is a Flask decorator used to map a URL to a Python function.
# '/students' is the URL (endpoint) that users access.
# methods=['GET'] allows only GET requests to retrieve student data.

@app.route('/students/<course>',methods=['GET'])
def get_student(course):
    print(course)
    students = [

        {
            "id": 101,
            "name": "Rishi",
            "age": 21,
            "course": "B.E Electronics and Telecommunication",
            "city": "Pune"
        },

        {
            "id": 102,
            "name": "Rahul",
            "age": 22,
            "course": "BCA",
            "city": "Nagpur"
        },

        {
            "id": 103,
            "name": "Sneha",
            "age": 20,
            "course": "B.Tech CSE",
            "city": "Mumbai"
        },

        {
            "id": 104,
            "name": "Amit",
            "age": 23,
            "course": "MCA",
            "city": "Delhi"
        }

    ]

    return students


#  Start the Flask application in debug mode when this file is run directly.
if __name__=='__main__':
    app.run(debug=True)
