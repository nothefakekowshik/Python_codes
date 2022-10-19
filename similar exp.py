import string

'''for ind, char in enumerate(string.ascii_lowercase):
    locals()[char] = 1 if ind == 0 else 10**ind'''
t = int(input())
while t:
    s1 = input()
    s2 = input()
    for i in range(len(s1)):
        if(s1[i].isalpha()==True):
            x=s1.replace("s1[i]","2")
    print(x)

    '''if (eval(s1) == eval(s2)):
        print("YES")
    else:
        print("NO")'''
    t -= 1

