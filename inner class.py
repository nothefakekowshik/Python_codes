class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def show(self):
        print(self.name,self.roll)
    class laptop:
        def __init__(self,brand,ram):
            self.brand=brand
            self.ram=ram
        def show(self):
            print(self.brand,self.ram)
s1=student('kowshik',2)
s1.show()
l1=student.laptop('hp',8)
l1.show()