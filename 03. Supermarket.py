from collections import deque

clients = deque()

while True:
    name = input()
    if name == 'End':
        print(f'{len(clients)} people remaining.')
        break
    elif name == 'Paid':
        while clients:
            print(clients.pop())
    else:
        clients.appendleft(name)

