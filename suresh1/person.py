class person1:
    def __init__(self,name,job=None,pay=0):
        self.name=name
        self.job=job
        self.pay=pay
    def giveraise(self,per):
        self.pay=int(self.pay+(self.pay*.10))
    def __repr__(self):
        return'[person:%s,%s,%s]'%(self.name,self.job,self.pay)


class manager(person1):
    def __init__(self,name,pay):
        person1.__init__(self,name,'mgr',pay)
    def giveraise(self,per,bonus=.10):
        person1.giveraise(self,per+bonus)
class department:
    def __init__(self,*args):
        self.members=list(args)
    def addmembers(self,person):
        self.members.append(person)
    def giveraise(self,per):
        person1.giveraise(per)

    def showall(self):
        for p in self.members:
            print(p)
if __name__=='__main__':
    p=person1('suresh','developer',10000.00)
    p1=manager('axness',20000)
    p3=manager('mallesh',22000)
    p4=person1('sai','hr',30000)
    #print(p)
    p3.giveraise(.10)
    #print(p3)
    p2=department(p1,p,p4)
    p2.addmembers(p3)
    p2.showall()

