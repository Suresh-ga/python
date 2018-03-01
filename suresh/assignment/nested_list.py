a=[[1,15],[3,5],[10,11,12]]
b=[]
for i in a:
    for j in i:
        b.append(j)
print(b)
c=[10,[20,30],40,50,[60,70,80],90]
d=[]
for i in c:
    if(isinstance(i,list)):
        for j in i:
            d.append(j)
    else:
         d.append(i)
print(d)



