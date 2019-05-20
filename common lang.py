nam=[]
lan=[]
f={}
c=0
g=""
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
lan2=" ".join(lan)
print(lan2)
print(type(lan2))
y=lan2.split()
y.sort()
print(enumerate(y))
c =""
for k in y:
    if k != c:
        count = [i for i, w in enumerate(y) if w == k]
        print(k + " frequency is " + str(len(count)))
    c = k
