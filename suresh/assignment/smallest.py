a=int(input('enter the value'))
b=int(input('enter the value'))
c=int(input('enter the value'))
d=int(input('enter the value'))
if(a is b or  a is c or a is d or b is c or b is d or c is d):
    print('invalid input')
elif(a<b and a<c and a<d):
    print('a is smallest')
elif(b<c and b<d):
    print('b is smallest')
elif(c<d):
    print('c is smallest')
else:
    print('d is smallest')