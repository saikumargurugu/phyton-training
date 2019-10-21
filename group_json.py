import json
from itertools import groupby

s=[
    {"sam":"dsdsdsd",
     "id":"22",
     "data":"sses13322", 
     "cato":"5543"},

    {"sam":"aaaaaa",
     "id":"22",
     "data":"sses13322", 
     "cato":"5543"},

    {"sam":"bbbbb",
     "id":"23",
     "data":"sses13322", 
     "cato":"554"},

   {"sam":"cccccc",
     "id":"23",
     "data":"sses13322", 
     "cato":"5543"},

   {"sam":"dddddd",
     "id":"24",
     "data":"sses13322", 
     "cato":"5543"}
]
l= json.dumps(s)
m= json.loads(l)
f={}
l=[]
e=[]
m.sort(key=lambda content: content['id'])
groups = groupby(m, lambda content: content['id'])
for k,v in groups:
    for m in v:
      l.append(str(m))
    f[k]=l
    l=[]
e.append(f)
print(json.dumps(e))
