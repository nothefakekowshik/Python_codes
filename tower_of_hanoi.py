def check(n,fromm,to,aux):
    if(n==1):
        print("move from ",fromm,"to",to)
        return
    check(n-1,fromm,aux,to)
    print("move n from ",fromm,"to",to,"using ",aux)
    check(n-1,aux,to,fromm)

n=3
check(n,'A','C','B')
