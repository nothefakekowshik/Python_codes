
# a=[9,10,15,30,45,56,72,88,100]
# low=0
# high=len(a)-1
# target=100
# flag=False
# while(low <= high):
#     centremid=(low+high)//2
#     leftmid=(low+centremid)//2
#     rightmid=(centremid+high)//2

#     if(a[centremid]==target):
#         flag=True
#         print("fount at "+str(centremid))
#         break
#     if(a[leftmid]==target):
#         flag=True
#         print("fount at "+str(leftmid))
#         break
#     if(a[rightmid]==target):
#         flag=True
#         print("fount at "+str(rightmid))
#         break    

#     elif(a[centremid] > target and a[leftmid] > target):
#         high=leftmid-1
#     elif(a[centremid] > target and a[leftmid] < target):
#         low=leftmid+1
    
#     elif(a[centremid] < target and a[rightmid] > target):
#         high=rightmid-1
#     elif(a[centremid] < target and a[rightmid] < target):
#         low=rightmid+1

# if(flag==False):
#     print("Not found")



a=[9,10,15,30,45,56,72,88,100]
flag=False
for target in a:
    low=0
    high=len(a)-1
    while(low <= high):
        centremid=(low+high)//2
        leftmid=(low+centremid)//2
        rightmid=(centremid+high)//2

        if(a[centremid]==target):
            flag=True
            print("found %d at %d " % (target,centremid))
            break
        if(a[leftmid]==target):
            flag=True
            print("found %d at %d " %(target,leftmid))
            break
        if(a[rightmid]==target):
            flag=True
            print("found %d at %d " %(target,rightmid))
            break    

        elif(a[centremid] > target and a[leftmid] > target):
            high=leftmid-1
        elif(a[centremid] > target and a[leftmid] < target):
            low=leftmid+1
        
        elif(a[centremid] < target and a[rightmid] > target):
            high=rightmid-1
        elif(a[centremid] < target and a[rightmid] < target):
            low=rightmid+1

    if(flag==False):
        print("Not found")