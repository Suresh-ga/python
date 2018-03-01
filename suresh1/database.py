from suresh1.person import person1,manager
p1=person1('suresh','manager',25000)
p2=person1('ramesh','developer',40000)
p3=manager('axness',30000)
import shelve
db=shelve.open('persondata')
for obj in (p1,p2,p3):
    db[obj.name]=obj
db.close()
db=shelve.open('persondata')
print(len(db))
print(tuple(db.values()))
print(tuple(db.keys()))
print(db['suresh'])
p1=db['axness']
p1.giveraise(.10)
print(p1)
for i in db:
    print(i,'==',db[i])
for j in sorted(db):
    print(j,'==',db[j])
