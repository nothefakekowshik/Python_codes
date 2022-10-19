from math import floor, sqrt
def algo(limit, primes):
    mark = [False]*(limit+1)
    for i in range(2, limit+1):
        if not mark[i]:
            primes.append(i)
            for j in range(i, limit+1, i):
                mark[j] = True
def printPrimes(low, high):
    arr=[]
    limit = floor(sqrt(high)) + 1
    primes = list()
    algo(limit, primes)
    n = high - low + 1
    mark = [False]*(n+1)
    for i in range(len(primes)):
        loLim = floor(low/primes[i]) * primes[i]
        if loLim < low:
            loLim += primes[i]
        if loLim == primes[i]:
            loLim += primes[i]
        for j in range(loLim, high+1, primes[i]):
            if j != primes[i]:
                mark[j-low] = True
    for i in range(low, high+1):
        if not mark[i-low]:
            arr.append(i)
    for i in arr:
        if(i!=1):
            print(i)
    print()
t=int(input())
while t:
	t-=1
	m,n=list(map(int,input().split()))
	printPrimes(m,n)