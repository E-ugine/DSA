#JSON is a syntax for storing and exchanging data
#It's a text written with Javascript object notation
#Use case

import json

x = '{ "name":"John", "age":30, "city":"New York"}' #This is json data
y = json.loads(x)

#Prints a Python dictionary
print(y["age"])

#Converting from Python to JSON
#Python object[Dict]

x = {
    "Age": 36,
    "Name": "Eugine",
    "Role": "Systems Engineer"
}
#converting to json
y = json.dumps(x)
print(y)
