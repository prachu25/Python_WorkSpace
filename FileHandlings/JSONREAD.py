import json

# json.load() - convert json file into python dict

with open("user.json", "r") as file:
    data = json.load(file)

    for k,v in data.items():
        print(f"{k} : {v} ")


"""
# FOR WRITE

    json.dump()
       ↓
    Python data → JSON file
       ↓
    WRITE

    
    
# FOR READ

    json.load()
        ↓
    JSON file → Python data
        ↓
    READ

"""