i= int(input("enter the number"))
k=2
if i % 2 == 0 or i % 2 == 1 :
    if k  < i:
         while i % k != 0:
             print("enterd number is prime")
             break
         else:
            if k != i:
                print("enterd number is not prime")