import math
def primeFactors(prime,n):

    while n % 2 == 0:
        prime.append(2)
        n = n //2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            prime.append(i)
            n = n // i
    if n > 2:
        prime.append(n)

n = 15
prime=[]
primeFactors(prime,n)
print(max(prime))
