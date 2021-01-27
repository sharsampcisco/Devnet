import json

UserB = '{"Name" : "Rohan", "Age": 25, "Skills": ["php", "networking"], "Location" : "Bangalore"}'
jsonobj = json.loads(UserB)
print(jsonobj['Name']+"'s age is : ",jsonobj['Age'])