p=["Name","destignation","age","salary"]
a=["neelam","programer","24","2400",]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"]
v={}  
k={}
s={}
t={}
i=0
while i<len(p):
    k[p[i]]=a[i]
    v[p[i]]=b[i]
    s[p[i]]=c[i]
    t[p[i]]=d[i]
    i+=1
# print(k)
# print(v)
# print(s)
# print(t)
j=0
r={}
while j<len(p):
    r["emp1"]=k
    r["emp2"]=v
    r["emp3"]=s
    r["emp4"]=t
    j+=1
print(r)





