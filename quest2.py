import json
a={"name": "David",
"class":"I",
"age": 6  
 }
b=open("quest2.json","+r")
json.dump(a,b,indent=4)

# c=json.dump(a)
# print(c)
