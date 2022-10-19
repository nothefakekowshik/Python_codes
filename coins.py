print("Enter the number of 1 and 5 coins and total amount")
x,y,z=list(map(int,input().split()))
five_remainder=z//5  #21//5
if(y*5 +x*1 <z):
    print("-1")
else:
    print(z-five_remainder*5) #21-4*5
    print(five_remainder)
    

