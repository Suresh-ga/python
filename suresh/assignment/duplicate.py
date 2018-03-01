l=[10,20,100,50,40,60,90,20,200]
a=[]
for i in l:
    if(i in a):
        continue
    else:
        if(l.count(i)==2):
            a.append(i)
            print(a)




    l.sort()
print('the second largest element is==',l[-2])


