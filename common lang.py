nam=[]
lan=[]
for i in range(0,10):
    n=input("enter the name[end to stop]")
    if n == "end":
        break
    else:
        while 1:
            nam.append(n)
            m=input(".........enter known langauge[end to stop]")
            if m == "end":
                break
            else:
                lan.append(m)
lan.sort()
c =""
for k in lan:
    if k != c:
        count = [i for i, w in enumerate(lan) if w == k ]
        print(k + " frequency is " + str(len(count)))
    c = k
