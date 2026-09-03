import json

data = {

    "userid": 101,
    "userName": "Joe Root",
    "Password": "liverpool",
    "userType": "student"
}

# dump - covert python data into JSON format

with open("user.json", "w") as file:
    json.dump(data, file, indent=5)











# take data and write it into file

# json.dump(data, file, indent=5)
#           ↓      ↓       ↓
#          WHAT   WHERE   HOW

# without indent - data will be in one line 
# with indent - data will be formating 
"""like this
{
     "userid": 101,
     "userName": "Joe Root",
     "Password": "liverpool"
}"""