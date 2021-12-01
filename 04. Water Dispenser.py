from collections import deque
water = int(input())
ppl = deque()
while True:
    cmd = input()
    if cmd == 'Start':
        break
    ppl.append(cmd)
while True:
    cmd = input()
    if cmd == 'End':
        break
    elif cmd.startswith('refill'):
        data = cmd.split(' ')
        water += int(data[1])
    else:
        # name = ppl.popleft()
        if water >= int(cmd):
            print(f'{ppl.popleft()} got water')
            water -= int(cmd)
        else:
            print(f'{ppl.popleft()} must wait')

print(f'{water} liters left')