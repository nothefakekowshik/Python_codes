class demo:
    def __init__(self,s1,s2):
        self.s1=[]
        self.s2=[]

    def insert_into(self,x):
        while(len(self.s1)!=0):
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while(len(self.s2)!=0):
            self.s1.append(self.s2.pop())
            
    def dequeue_into(self):
        if(len(self.s1)!=0):
            self.s1.pop()

    def display(self):
        print(self.s1)

        
s1=[]
s2=[]
obj=demo(s1,s2)
obj.insert_into(2)
obj.insert_into(1)
obj.insert_into(4)
obj.insert_into(5)
obj.dequeue_into()
obj.display()