from suresh1.person import person1
class test:
 if __name__=='__main__':
    p1=person1('suresh','developer',45000)
    print(p1)
    p1.giveraise(10)
    print(p1)
    print(p1.__class__.__name__)
    print(p1.__dict__)
    print(p1.__dict__.keys())
    for k in p1.__dict__:

        print(k,'==',p1.__dict__[k])
    for j in p1.__dict__:
        print(j,'==',getattr(p1,j))