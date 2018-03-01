while(True):
    a=input('enter the your option f or m')
    if(a=='m' or a=='f'):
        age=int(input('enter the age'))
        if(age>18 and age<21 and a=='m'):
            print("he is eligible for drinking")
        elif(age>21  and a=='m'):
            print('he is elifible for drinking and marriage')
        elif(age>18 and a=='f'):
            print('she is eligible for drinking and marriage')


