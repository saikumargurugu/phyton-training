k=s=0
a=[]
print("enter numbers that are to be sorted and [00 to exit]:")
while 1:
    try:
        k=int(input(""))
        if k != 00:
            a.append(k)
            print("the sorted list is ")
            a=sorted(a)
            print(a)
        else:
            break
    except:
        pass
for i in range(0,len(a)):
    s=s+a[i]
print("the sorted input list is:", a)