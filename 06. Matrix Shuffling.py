n, m = [int(x) for x in input().split()]
matrix = []
for _ in range(n):
    matrix.append([x for x in input().split()])
while True:
    line = input()
    if line == 'END':
        break
    cmd = line.split()
    if not (cmd[0] == 'swap' and len(cmd) == 5):
        print('Invalid input!')
        continue
    r1, c1, r2, c2 = [int(x) for x in cmd[1:]]
    # r1 = int(cmd[1])
    # c1 = int(cmd[2])
    # r2 = int(cmd[3])
    # c2 = int(cmd[4])
    if not (n >= r1 >= 0 and m >= c1 >= 0 and n >= r2 >= 0 and m >= c2 >= 0):
        print('Invalid input!')
        continue
    else:
        matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
        for row_elements in matrix:
            print(' '.join(x for x in row_elements))