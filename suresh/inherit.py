class inherit1:
    def __init__(self,name,age,sal):
        self.name=name
        self.age=age
        self.sal=sal
        print(name,age,sal)
    def lastname(self,name):
        return self.name.split()[-1]
    def incriment(self,per):
        self.sal=(int(self.sal*(1+per)))
    def __repr__(self):
        return '[inherit1:%s,%s,%s]'%(self.name,self.age,self.sal)
#if __name__=='__main__':
 #   a=inherit1('suresh',35,400000.00)
  #  a.incriment(10)
   # print(a.sal)

class inherit2(inherit1):
    def incriment(self,per,bonus=.10):
       inherit1.incriment(self,per+bonus)
if __name__=='__main__':
    b=inherit2('suresh1',23,30000.00)
    b.incriment(.10)
    print(b)
    print(b.sal)






