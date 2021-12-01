from collections import deque
food = int(input())
orders = deque(map(int, input().split()))
print(max(orders))
while orders:
    serv = orders[0]
    if serv <= food:
        food -= serv
        orders.popleft()
    else:
        break
if orders:
    print(f'Orders left: {" ".join(map(str, orders))}')
else:
    print('Orders complete')