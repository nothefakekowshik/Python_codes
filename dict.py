n=int(input())
students={}
averagedict={}
for _ in range(n):
    name,*line=input().split()
    marks=list(map(float,line))
    students[name]=marks
print(students)
for name,marks in students.items():
    averagedict[name]=sum(marks)/len(marks)
print(averagedict)