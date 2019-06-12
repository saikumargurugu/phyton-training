p=open(r"phbook.txt","at")
l=[]
f={}
while 1:
    i=input("enter name [end to stop]")
    if i != "end":
        if i in l:
            try:
                k = input("enter phno2")
                if len(k) == 10:
                    f[i].append(k)
                    l.append(f)
                else:
                    print("A ph no must have minimum 10 digits!")
            except:
                print("invalid input!")
                continue
        if i not in l:
            f[i]=[]
            k=input("enter phno")
            try:
                if len(k) == 10:
                    f[i].append(int(k))
                    l.append(f)
                    f={}
                else:
                    print("A ph no must have minimum 10 digits!")
            except:
                print("invalid input!")
                continue
    else:
        break
p.write(str(l)+ "\n")
p.close()
p=open(r"phbook.txt","rt")
k=input("enter the name to search")
r=p.readline()
for k in p:
    if k in r:
        print(k)