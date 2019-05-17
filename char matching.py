k= input("enter the first string")
l= input("enter the second string")

for i in range(0, len(l)):
    for j in range(0,len(k)):
        if l[i]==k[j] and l[i] != ' ':
             print( l[i],j)