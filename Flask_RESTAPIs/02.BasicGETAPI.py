from flask import Flask
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)

class BasicREST(Resource):
    def get(self):
        profile={
            "number":9,
            "name":"joe",
            "codename":"ethan",
            "city": "london",
            "language":"engllsh",
            "gender":"male",
            "dob":"9 june",
            "qualifilaction":"BFA",
            'email':"joe@gmail.com",
            "mobile":"8898976789",
            "keyskills":["java","python","sql"],
            "hobbies":["movies","music",'drawing']

        }

        return profile
    

api.add_resource(BasicREST,"/profile")
app.run(debug=True)