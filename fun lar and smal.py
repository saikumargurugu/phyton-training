def large_small(i):
    j=sorted(i)
    return j
k=[]
while 1:
    l= int(input("enter nmbers in list[submit to stop]"))
    if l == 00:
        break
    else:
        k.append(l)
k=large_small(k)
print("largest is",k[0],"smallest is",k[-1])