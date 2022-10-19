class student:
    school="PVPSIT"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        a=(self.m1+self.m2+self.m3)/3
        print(a)
    @classmethod
    def school(cls):
        return cls.school
    @staticmethod
    def info():
        print("this is static method")
s1=student(100,100,100)
s1.avg()
print(student.school())
s1.info()