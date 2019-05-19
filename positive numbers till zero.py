k=[]
while 1:
    c=int(input("enter a number:"))
    if c!=0:
        k.append(c)
    else:
        break
for i in range(0,len(k)):
    if k[i]>0:
        print("the positive number:",k[i])