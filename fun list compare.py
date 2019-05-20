def list_compare(i,j):
    c=True
    for m in range(0,len(i)):
        if i[m] == j[m]:
            c = True
        else:
            c = False
        return c
k=[]
l=[]
while 1:
    i=input("enter the value for list 1 [end when done]")
    if i=="end":
        break
    else:
        k.append(i)
while 1:
    i = input("enter the value for list 2 [end when done]")
    if i == "end":
        break
    else:
        l.append(i)
if len(k)==len(l):
    b=list_compare(k,l)
    print(b)
else:
    print("False")