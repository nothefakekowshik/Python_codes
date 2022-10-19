a=[-6,3,-2,-9,5,9,-4,-2,5,5]
double_list=[]
single_list=[]
for i in a:
    if(a.count(i)>1):
        double_list.append(i)
    else:
        single_list.append(i)

single_list.sort()
double_list.sort(reverse=True)
double_list.extend(single_list)
print(*(double_list))














# n=int(input())
# a=[-6,3,-2,-9,5,9,-4,-2,5,5]
# a.sort()
# val=sorted(a,key=a.count)
# val.sort(reverse=True)
# print(val)