'''

A big ship with numerous passengers is sinking, and there is a need to evacuate these people with the minimum number of life-saving boats. Each boat can carry, at most, two persons however, the weight of the people cannot exceed the carrying weight limit of the boat.

We are given an array, people, where people[i] is the weight of the ith person, and an infinite number of boats, where each boat can carry a maximum weight, limit. Each boat carries, at most, two people at the same time. This is provided that the sum of the weight of these people is under or equal to the weight limit.
 
'''

def rescue_boats_one_pointer(people, limit):
    people.sort()
    curr_sum = 0
    ans = 0
    i = 0
    while i < len(people):
      if curr_sum + people[i] > limit:
        ans += 1
        curr_sum = 0
      curr_sum += people[i]
      i+=1
    if curr_sum > 0:
      ans += 1
    return ans
    # this will fail because a boat can only hold max of 2 people.


def rescue_two_pointers(people,limit):
    people.sort()
    left = 0
    right = len(people) - 1
    boats = 0  
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1  
        right -= 1
        boats += 1 
    return boats

