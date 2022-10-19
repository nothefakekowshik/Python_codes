# def gcd(a,b):
#     if(a==0):
#         return b
#     else:
#         return gcd(b%a,a)

# a=int(input())
# b=int(input())

# gcdans=gcd(a,b)
# print("gcd is %d"%(gcdans))
# print("Lcm is %d"%((a*b)/gcdans))


























def gcd(a,b):
    if(a==0):
        return b
    return gcd(b%a,a)

a=8
b=2
print(gcd(a,b))