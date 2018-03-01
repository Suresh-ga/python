l=[i*i if i%2==0 else i**3 for i in range(1,101) if i%3!=0]
print(l)
a=[1,2,3,4]
b=['A','B','C','D']
c=[[n,l] for n  in a for l in b]
print(c)