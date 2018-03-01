class student1:

    def __init__(self,name=None,rollno=0,avg=0):
        self.name=name
        self.rollno=rollno
        self.avg=avg
        self.name = input('enter name==')
        self.rollno = input('enter roll no==')
        s = 0
        for i in range(3):
            m1 = int(input('enter marks=='))
            s = s + m1
        aa = s / 3
        self.avg = aa

    def __repr__(self):
        return '[student1:%s,%s,%s]' % (self.name, self.rollno, self.avg)



class student2(student1):

     def __init__(self,grade=None, name=None,rollno=0,avg=0):

         student1.__init__(self,name=None,rollno=0,avg=0)
         self.grade=grade
         if (self.avg >= 91 and self.avg<= 100):
             self.grade='A+'
         elif (self.avg>= 81 and self.avg<= 90):
             self.grade = 'B'
         elif (self.avg >= 71 and self.avg<= 80):
             self.grade = 'B+'
         elif (self.avg>= 61 and self.avg <= 70):
             self.grade = 'B'
         elif (self.avg >= 51 and self.avg<= 60):
             self.grade = 'C+'
         elif (self.avg>= 41 and self.avg<= 50):
             self.grade = 'C'
         elif (self.avg >= 0 and self.avg<= 40):
             self.grade = 'F'
         else:
             self.grade="Strange Grade..!!"


     def __repr__(self):
        return '[student:%s,%s,%s,%s]'%(self.name,self.rollno,self.avg,self.grade)
if __name__=='__main__':
    a=student2()
    b=student2()
    print(a)
    print(b)
import shelve
d=shelve.open('student')
for obj in (a,b):
    d[obj.name]=obj
d.close()
d=shelve.open('student')
print(len(d))
print(list(d.keys()))
print(list(d.values()))


