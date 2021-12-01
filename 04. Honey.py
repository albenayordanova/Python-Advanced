from collections import deque
bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
sequence_of_symbols = deque(input().split())
ttl = 0
while bees and nectar:
    if nectar[-1] < bees[0]:
        nectar.pop()
    else:
        sign = sequence_of_symbols.popleft()
        if sign == '+':
            ttl += abs(bees.popleft() + nectar.pop())
        elif sign == '-':
            ttl += abs(bees.popleft() - nectar.pop())
        elif sign == '*':
            ttl += abs(bees.popleft() * nectar.pop())
        elif sign == '/':
            ttl += abs(bees.popleft() // nectar.pop())

print(f'Total honey made: {ttl}')
if bees:
    print(f'Bees left: {", ".join(str(x) for x in bees)}')
if nectar:
    print(f'Nectar left: {", ".join(str(x) for x in nectar)}')

# 30
# 15 9 5 150 8
# * + + * -

# 20 62 99 35 0 150
# 120 60 10 1 70 10
# + - + + / * - - /