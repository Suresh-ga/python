from abc import ABCMeta,abstractmethod
class abst1(metaclass=ABCMeta):
    @abstractmethod
    def m1(self):
        pass
    def m2(self):
        print("this is parent class method")
class abst2(abst1):
    def m1(self):
        print('this is sub class method')
if __name__=='__main__':
    a=abst2()
    a.m1()
    a.m2()
