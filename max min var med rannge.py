k=[]
v=[]
a=0
while 1:
    c=int(input("enter a number:"))
    if c!=0:
        k.append(c)
    else:
        break
print("maxmium value",max(k))
print("minium value",min(k))
print("range is", min(k),"-",max(k))
for l in range(0,len(k)):
    a=k[l]-(sum(k)/(len(k)))
    v.append(a*a)
print("variance is",sum(v)/(len(k)-1))
if len(k) % 2 == 0:
    print("media is",(k[(len(k)//2)] + k[(len(k)//2)-1])/2)
else:
    print("median is",k[(len(k)//2)])
