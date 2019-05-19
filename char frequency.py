s = input("enter a string")

f = {}
for i in s:
    if i in f:
        f[i] += 1
    else:
        f[i] = 1
print("Count of all characters in string is :\n "
      + str(f))