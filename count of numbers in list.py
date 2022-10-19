a=[1,2,3,5,2,9,7,3,5]
b=[]
for i in a:
    if i not in b:
        print("%d occurs %d times"%(i,a.count(i)))
        b.append(i)
