b={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
# k={}
# for i in sorted (b.values()):
#     k[i]=b.values
#     print(k)
import json
# b={"name":"kajal",
# "age":21}
# c=open("ishi.json","w")
# json.dump(b,c,indent=4)
# k=json.dumps(b)
# print(k)
# print(type(k))

k=json.dumps(b,sort_keys=True)
print(k)