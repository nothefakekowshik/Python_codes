a=[7,0,25,6,16,17,0]
my_dict={}
for i in a:
    if i not in my_dict:
        my_dict[i]=1
    else:
        my_dict[i]+=1
count=0
for i in sorted(my_dict.keys()):
    print(i,my_dict[i])

