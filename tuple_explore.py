a=[]
for i in range(2):
    demo_tuple=()
    demo_list=[]
    name=input("Enter name")
    age=int(input("Enter age"))
    demo_list.append(name)
    demo_list.append(age)
    demo_tuple=tuple(demo_list)
    a.append(demo_tuple)
print(a)