class decarators1:
    def check(func):
        def inner(self,a,b):
            if b==0:
                print ("b nalue must be grater then zero")
                return
            return func(a,b)
        return inner
    @check
    def division(a,b):
        print(a/b)
        return a/b
if __name__=='__main__':
    x=decarators1()
    x.division(10,2)

class decarators2:

    def star(func):
        def inner(*args):
            print('*'*30)
            func(*args)
            print('%'*30)
        return inner
    def percent(func):
        def inner(*args):
            print('%'*30)
            func(*args)
            print('%'*30)
        return inner

    @star
    @percent
    def printer(self, *args):
        print(args)
if __name__=='__main__':


    b=decarators2()
    b.printer('hello')
    b.printer('hello','world')
class decarators3:
    def make_pretty(func):
        def inner(self):
            print('i got decarated')
            func(self)
        return inner

    @make_pretty
    def ordinary(self):
        print('i am ordinary')
if __name__=='__main__':
    c=decarators3()
    c.ordinary()


