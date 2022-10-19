def calc(str,l,r):
    if(l==r):
        print(''.join(str))
    else:
        for i in range(l,r+1):
            str[l],str[i]=str[i],str[l]
            calc(str,l+1,r)
            str[l],str[i]=str[i],str[l]



if __name__=="__main__":
    str='abc'
    calc(list(str),0,len(str)-1)
