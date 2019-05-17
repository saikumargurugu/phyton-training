k= input("enter the string")
for i in range(0, len(k)):
    if k[i]=='@':
        print("it is an perfect mail id")
        y= k.partition("@")
        print(y[2])
    else:
        print("pelse enter a valid mail id" )
        break