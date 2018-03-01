a=int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter c value"))
if(a==0 or (a>b and a>c)):
    print(' a is biggest')

if(b>a and b>c and a!=0):
    print('b is biggest')
if(c>a and c>b and a!=0):
    print('c is biggest')


