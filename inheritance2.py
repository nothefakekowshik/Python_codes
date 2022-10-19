class person:
    def details(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)

class employee(person):
    def details_employee(self,post):
        self.post=post