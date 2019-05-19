f={}
while 1:
    i=input("enter name")
    if i != "end":
            if i in f:
                f[i].append(input("enter phno2"))
            else:
                if i not in f:
                    f[i]=[]
                    f[i].append(input("enter phno"))
    else:
        break
for k,v in sorted(f.items()):
    print(k,":",', '.join(v))