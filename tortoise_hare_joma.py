#finding the duplicate number in o(n) time complexity
#array should from 1 to N

#a=[5,2,4,3,4]

a=[3,1,3,4,2]

tortoise=a[0]
hare=a[0]
while True:
    tortoise=a[tortoise]
    hare=a[a[hare]]
    if(tortoise==hare):
        break

ptr1=a[0]
ptr2=tortoise
while(ptr1!=ptr2):
    ptr1=a[ptr1]
    ptr2=a[ptr2]

print(ptr1)