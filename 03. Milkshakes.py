from collections import deque
chocolates = [int(x) for x in input().split(',')]
milk = deque(int(x) for x in input().split(','))
shakes = 0
while chocolates and milk and shakes < 5:
    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    if milk[0] <= 0:
        milk.popleft()
        continue
    if chocolates[-1] == milk[0]:
        shakes += 1
        chocolates.pop()
        milk.popleft()
    else:
        milk.append(milk.popleft())
        chocolates[-1] -= 5
if shakes < 5:
    print('Not enough milkshakes.')
else:
    print('Great! You made all the chocolate milkshakes needed!')
if chocolates:
    print(f'Chocolate: {", ".join([str(x) for x in chocolates])}')
else:
    print('Chocolate: empty')
if milk:
    print(f'Milk: {", ".join([str(x) for x in milk])}')
else:
    print('Milk: empty')

# 20, 24, -5, 17, 22, 60, 26
# 26, 60, 22, 17, 24, 10, 55
# -10, -2, -30, 10
# -5