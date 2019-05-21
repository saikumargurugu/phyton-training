def primeno(i):
    if i % 2 == 0 or i % 2 == 1:
        for k in range(2, i - 1):
            if i % k == 0:
                return False
            elif k == i - 2:
                return True
j=[]
while 1:
    k=int(input("enter numbers[000 to end]"))
    if k!= 000:
        j.append(k)
    else:
        break
for m in filter(primeno,j):
    print(m, end=" ")