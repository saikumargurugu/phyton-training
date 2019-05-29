class Accounts:
    def __init__(self,name,id,des,sal,k):
        f={}
        self.f=name
        self.id=id
        self.des=des
        self.sal=sal
        self.k=k
        print(len(name))
        for i in range(1,k):
            f[name[i]]=id
            f[name[i]]=des
            f[name[i]]=sal

    def show_det(self,f,id,des,sal):
        return self.f #,self.id,self.des,self.sal
        #return Accounts()
m=[]
a=n=d=s=[]
k=0
print("select your option \n 1. create an account\n 2.show salary \n 3.change job \n 4.exit")
while 1:
    i=int(input())
    if i== 4:
        break
    if i==1:
        k+=1
        a.append(input("enter acc holder:"))
        n.append((input("enter id [nums only]")))
        d.append(input("enter designation"))
        s.append(input("enter salary:"))
m=Accounts(a,n,d,s,k)
print(type(m))

print(m.show_det(a,n,d,s))

