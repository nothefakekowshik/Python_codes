import math


print("Mid 1")
print("----")
t_one_desc1=int(input("Enter the descriptive marks of T1"))
t_one_obj1=int(input("Enter the obj marks of T1"))


# t_two_desc1=int(input("Enter the descriptive marks of T2"))
# t_two_obj1=int(input("Enter the obj marks of T2"))

# t_three_desc1=int(input("Enter the descriptive marks of T3"))
# t_three_obj1=int(input("Enter the obj marks of T3"))

# t_four_desc1=int(input("Enter the descriptive marks of T4"))
# t_four_obj1=int(input("Enter the obj marks of T4"))


# t_five_desc1=int(input("Enter the descriptive marks of T5"))
# t_five_obj1=int(input("Enter the obj marks of T5"))


print("Mid 2")
print("----")
t_one_desc2=int(input("Enter the descriptive marks of T1"))
t_one_obj2=int(input("Enter the obj marks of T1"))

# t_two_desc2=int(input("Enter the descriptive marks of T2"))
# t_two_obj2=int(input("Enter the obj marks of T2"))

# t_three_desc2=int(input("Enter the descriptive marks of T3"))
# t_three_obj2=int(input("Enter the obj marks of T3"))

# t_four_desc2=int(input("Enter the descriptive marks of T4"))
# t_four_obj2=int(input("Enter the obj marks of T4"))

# t_five_desc2=int(input("Enter the descriptive marks of T5"))
# t_five_obj2=int(input("Enter the obj marks of T5"))

t_one_avg=math.floor(t_one_desc1+t_one_desc2/2)+math.floor(t_one_obj1+t_one_obj2/2)
print(t_one_avg)
