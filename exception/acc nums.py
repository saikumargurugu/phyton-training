k=s=0
a=[]
print("enter 10 numbers")
while 1:
    try:
        k=int(input(""))
        a.append(k)
        if len(a)>=10:
            break
    except:
        pass
for i in range(0,len(a)):
    s=s+a[i]
print(s)