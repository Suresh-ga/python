import copy
l=[1,2,3,4,5,[6,7,8]]
l1=l
l1.append('22')
print(l,l1)
l2=l.copy()
l2.append(25)
print(l,l2)
del(l2[5][1])
print(l,l2)
l3=copy.deepcopy(l)
l3.append(45)
print(l,l3)
del(l3[5][1])
print(l,l3)




