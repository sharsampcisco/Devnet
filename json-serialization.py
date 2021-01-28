import json

UserA = {
    "Name" : "Vandana",
    "Age" : 26,
    "Skills" : ['python','c++','networking'],
    "Location" : "Bangalore"
}
jsonstring = json.dumps(UserA)
print("First user's detail is : "+jsonstring)

"""
To make it fail uncomment the below
"""
#print(jsonstring['Name']) 
#print(type(jsonstring))

#Uncomment below to Deserialize 
jsonobj = json.loads(jsonstring)
print(jsonobj['Name']+"'s Age is : ", jsonobj['Age'])

