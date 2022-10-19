import heapq

a=[5,7,9,1,3]

k=3

heapq.heapify(a)

for i in range(k-1):
    heapq.heappop(a)
    
print(a)
