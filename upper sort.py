def uppercase(n):
    return n.isupper()
i= input("enter the string with both upper & lower case letters")
for m in filter(uppercase,i):
    print(m, end=" ")