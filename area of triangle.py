a=int(input("enter the side a"))
b=int(input("enter the side b"))
c=int(input("enter the side c"))
print("a={:d},b={:d},c={:d}".format(a,b,c))
s=int(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("s={:f},area= {:f}".format(s,area))
