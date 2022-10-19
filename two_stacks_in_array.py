class twostacks():
    def __init__(self,n):
        self.size=n
        self.top1=-1
        self.top2=n
        self.a=[None]*n

    def push1(self,x):
        if(self.top2-self.top1>=0):
            self.top1+=1
            self.a[self.top1]=x
        else:
            print("Overflow beech")
            exit(1)          

    def push2(self,x):
        if(self.top2-self.top1>=0):
            self.top2-=1
            self.a[self.top2]=x
        else:
            print("Overflow beech")
            exit(1)          
    def pop1(self):
        if(self.top1>=0):
            popped_val=self.a[self.top1]
            self.top1-=1
            return popped_val
        else:
            print("Over flow beech")
        
    def pop2(self):
        if(self.top2<self.size):
            popped_val=self.a[self.top2]
            self.top2+=1
            return popped_val
        else:
            print("Over flow")


ts=twostacks(5)
ts.push1(5)
ts.push2(10)
ts.push2(15)
ts.push1(11)
ts.push2(7)
print("Popped element from stack1 is " + str(ts.pop1()))
ts.push2(40)
print("Popped element from stack2 is " + str(ts.pop2()))