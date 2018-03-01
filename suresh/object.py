from suresh.object1 import sample1
class sample:
 'sample class for oops'
 name='suresh'
 age=95
 if __name__=='__main__':
  print(name)
  print(age)
#print(sample.__doc__)
#print(sample.__dict__)
#print(sample.__bases__)
a=sample()
a.name="sai"
a.age=20
print(a.__dict__.values())
print(a.__dict__.keys())
print(a.name)
print(a.age)
def uppercase(obj):
    return obj.name.upper()
sample.s=uppercase
print(sample.s(a))
print(a.s())
d=sample1('axness',45,3000.00)



