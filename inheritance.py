class A:
    def am(self):
        print('i am in a')
class B(A):
    def bm(self):
        super().am()
        print('i am in B')
#a=A()
b=B()
b.bm()
