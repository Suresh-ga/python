class getset1:
    def getage(self):
        age=40
        return age
    age=property(getage,None)
    def getname(self):
        name='suresh'
        return name
    name=property(getname,None)
if __name__=='__main__':
    a=getset1()
    print(a.age)
    print(a.name)