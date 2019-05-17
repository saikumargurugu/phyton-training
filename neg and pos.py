from array import*
h=0
c=0
a = array('i',[])
n=int(input("enter lenth nums"))
for i in range(n):
    b=int(input("enter num" ))
    a.append(b)
for i in range(n):
    if a[i] < 0:
        c+=1
    else:
        h+=1
print("negetives",c)
print("positive",h)
