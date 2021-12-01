# from collections import deque
# n = int(input())
# stations = deque()
# for _ in range(n):
#     pump = [int(x) for x in input().split()]
#     stations.append(pump)
#
# for attempt in range(n):
#     fuel = 0
#     completed = True
#     for petrol, distance in stations:
#         fuel += petrol
#         if distance > fuel:
#             completed = False
#             break
#         fuel -= distance
#     if completed:
#         print(attempt)
#         break
#     stations.append(stations.popleft())

from collections import deque
queue = deque()
n = int(input())
for _ in range(n):
    gas_pump = input().split()
    queue.append([int(gas_pump[0]), int(gas_pump[1])])
for i in range(n):
    fuel_tank = 0
    gas_pump_count = 0
    for gas_pump in queue:
        fuel, distance = gas_pump[0], gas_pump[1]
        fuel_tank += fuel
        if fuel_tank < distance:
            break
        fuel_tank -= distance
        gas_pump_count += 1
    if gas_pump_count == n:
        print(i)
        break
    queue.rotate(-1)