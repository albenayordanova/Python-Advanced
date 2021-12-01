import sys
from io import StringIO
t1 = '''3
1, 2, 3
4, 5, 6
7, 8, 9
'''
sys.stdin = StringIO(t1)

n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split(', ')])

primary_d = []
secondary_d = []
for r in range(n):
    primary_d.append(matrix[r][r])
    secondary_d.append(matrix[r][n - r - 1])
print(f'Primary diagonal: {", ".join([str(x) for x in primary_d])}. Sum: {sum(primary_d)}')
print(f'Secondary diagonal: {", ".join([str(x) for x in secondary_d])}. Sum: {sum(secondary_d)}')