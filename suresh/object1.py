class sample1:
    def __init__(self,name,age,sal):
        self.name=name
        self.age=age
        self.sal=sal
        print(name,sal,age)
    def lastname(self):
        return self.name.split()[-1]
    def increment(self,per):
       self.sal=int(self.sal*(1+per))
    def info(self):
        return (self.name,self.age,self.sal)
    def __repr__(self):
        return '[sample:%s,%s,%s]'%(self.name,self.sal,self.age)
if __name__=='__main__':
 a=sample1('suresh gopi',22,30000.00)
 b=sample1('sai kiran',23,20000)
 print(a.lastname())
 print(b.lastname())
 a.increment(10)
 b.increment(10)
 print(a)
 print(b)
 a.info()
 b.info()
 print(a.info)
 print(b.info)

