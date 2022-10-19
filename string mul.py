# User function Template for python3

def multiply(a, b):
    # add code here
    c = int(a) * int(b)
    print(c)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a, b = input().split()
        multiply(a, b)
