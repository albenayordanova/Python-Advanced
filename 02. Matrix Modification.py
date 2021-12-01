n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split()])
while True:
    line = input()
    if line == 'END':
        break
    cmd = line.split()
    act = cmd[0]
    r1, c1, value = cmd[1:]
    if int(r1) < 0 or int(c1) < 0:
        print('Invalid coordinates')
        continue
    if n <= int(r1) or n <= int(c1):
        print('Invalid coordinates')
        continue
    if act == 'Add':
        matrix[int(r1)][int(c1)] += int(value)
    elif act == 'Subtract':
        matrix[int(r1)][int(c1)] -= int(value)
for el in matrix:
    print(' '.join(str(x) for x in el))