class Accounts:
    def __init__(self,name,id,des,sal):
        self.name=name
        self.id=id
        self.des=des
        self.sal=sal

    def show_det(self,name,id,des,sal):
        return self.name ,self.id,self.des,self.sal

    def show_sal(self,name,sal):
        return self.name ,self.sal
    def add_hra_pf(self,name,sal):
       # HRA = (sal * 28) / 100
        #PF =  (sal * 2) / 100
        sal = sal*828/100
        return self.name,sal
a=d=""
n=s=m=0
while 1:
    i=int(input("select your option \n 1. create an account\n 2.show salary \n 3.change job \n 4.add intrest \n 5.exit\n"))
    if i== 5:
        break
    if i==1:
        a=input("enter acc holder:")
        n=int(input("enter id [nums only]"))
        d=input("enter designation")
        s=int(input("enter salary:"))
        m = Accounts(a, n, d, s,)
        print(m.show_det(a, n, d, s))
    if i==2:
        print(m.show_sal(a,s))
    if i==3:
        d=input("enter new job")
        m = Accounts(a, n, d, s,)
        print("job changed successfully",m.show_det(a, n, d, s))
    if i==4:
        print("salary after adding 30% HRA and 2% PF",m. add_hra_pf(a, s))










