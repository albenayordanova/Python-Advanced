from collections import deque

n, m = [int(x) for x in input().split()]
snake = input()
line = deque(snake)
temp = []
# matrix = []
for row in range(n):
    if row % 2 == 0:
        for col in range(m):
            x = line.popleft()
            temp.append(x)
            line.append(x)
        # matrix.append(temp)
        print(''.join(temp))
        temp = []
    else:
        for col in range(m):
            x = line.popleft()
            temp.append(x)
            line.append(x)
        temp = temp[::-1]
        # matrix.append(temp)
        print(''.join(temp))
        temp = []
