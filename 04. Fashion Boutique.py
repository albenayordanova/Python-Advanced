# clothes = [int(x) for x in input().split()]
# cap = int(input())
# temp = cap
# rack = 1
# while clothes:
#     last = clothes[-1]
#     if temp >= last:
#         temp -= last
#         clothes.pop()
#     else:
#         rack += 1
#         temp = cap
# print(rack)

from collections import deque
clothes = deque(map(int, input().split()))
max_weight = int(input())
weight = max_weight
rack = 1
while clothes:
    temp = clothes[-1]
    if weight <= temp:
        rack += 1
        weight = max_weight

    weight -= temp
    clothes.pop()
print(rack)