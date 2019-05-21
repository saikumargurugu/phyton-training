i= int(input("enter the number"))
if i % 2 == 0 or i % 2 == 1 :
    for k in range(2,i-1):
         if i % k == 0:
             print("enterd number is not prime")
             break
         elif k == i-2:
             print("enterd number is prime")
