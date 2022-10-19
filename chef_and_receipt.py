# 10
# 256
# 255
# 4096


menu_price=[1,2,4,8,16,32,64,128,256,512,1024,2048]
n=10
curr_price=0
for i in menu_price:
    if(i<=n):
        curr_price=i
    else:
        break
print(curr_price)
values=[]
values.append(curr_price)
if(n-curr_price in menu_price):
    values.append(n-curr_price)
if(sum(values)==n):
    print(len(values))
