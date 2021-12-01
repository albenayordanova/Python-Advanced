from collections import deque
data = input().split()
step = int(input())
queue = deque(data)
while queue:
    for _ in range(step - 1):
        # queue.append(queue.popleft())
        queue.rotate(-1)
    name = queue.popleft()
    if queue:
        print(f'Removed {name}')
    else:
        print(f'Last is {name}')