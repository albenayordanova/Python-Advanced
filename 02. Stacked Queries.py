# from collections import deque
n = int(input())
stack = []
for _ in range(n):
    cmd = input().split()
    data = cmd[0]
    if data == '1':
        stack.append(int(cmd[1]))
    elif data == '2':
        if stack:
            stack.pop()
    elif data == '3':
        if stack:
            print(max(stack))
    elif data == '4':
        if stack:
            print(min(stack))
while stack:
    el = stack.pop()
    if stack:
        print(el, end=', ')
    else:
        print(el)
