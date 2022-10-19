class demo:
    def __init__(self,s1,s2):
        self.s1=[]
        self.s2=[]

    def insert_into(self,x):
        self.s2.append(x)
        while(len(self.s1)!=0):
            self.s2.append(self.s1[0])
            self.s1.remove(self.s1[0])

        temp=self.s1
        self.s1=self.s2
        self.s2=temp

    def delete(self):
        if(len(self.s1)!=0):
            self.s1.remove(self.s1[0])

    def display(self):
        print(self.s1)


s1=[]
s2=[]
obj=demo(s1,s2)
obj.insert_into(3)
obj.insert_into(1)
obj.insert_into(4)
obj.insert_into(5)
obj.display()
obj.delete()
obj.display()
