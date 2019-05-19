print("enter 10 numbers")
k=[]
for i in range(1,10):
    c=int(input(""))
    k.append(c)
for i in range(0,len(k)):
    if k[i]==1:
        print("1 is neither odd nor even")
    if k[i] % 2 == 0:
        print("the eve numbers are", k[i])
    if k[i] % 2 != 0:
        print("the odd numbers are",k[i])



