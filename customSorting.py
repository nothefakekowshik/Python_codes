class demo:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __repr__(self):
        return repr(list((self.name,self.age)))

a =[
    demo("kowshik",21),
    demo("elon",60),
    demo("moksh",1)
]

a= sorted(a,key= lambda x : x.age)
print(a)
for i in a:
    print(i.name , i.age)