class car:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def output(self):
        print("car name is "+self.name+" color is "+self.color)

name=input("enter the car name")
color=input("enter the car color")
c=car(name,color)
c.output()