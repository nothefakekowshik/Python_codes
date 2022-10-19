num = int(input("Enter the number"))
length = len(str(num))
sum = 0
temp = num
while temp > 0:
   rem = temp % 10
   sum += rem**length
   temp //= 10

if(num == sum):
   print("Armstrong number")
else:
   print("Not Armstrong number")