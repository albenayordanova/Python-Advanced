import sys
from io import StringIO

t1 = '''3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0
'''
t2 = '''2, 4
10, 11, 12, 13
14, 15, 16, 17
'''
sys.stdin = StringIO(t1)
# sys.stdin = StringIO(t2)

# 80% - if you find more than one max square, print the top-left one
def read_matrix():
    n, m = [int(x) for x in input().split(', ')]
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
    return matrix


sums = []
matrix = read_matrix()
n = len(matrix)
m = len(matrix[0])
for r in range(n - 1):
    for c in range(m - 1):
        current_sum = matrix[r][c] + matrix[r][c + 1] + matrix[r + 1][c] + matrix[r + 1][c + 1]
        sums.append((current_sum, r, c))
max_sum = max(sums)
# print(max_sum)
r = max_sum[1]
c = max_sum[2]
print(matrix[r][c], matrix[r][c + 1])
print(matrix[r + 1][c], matrix[r + 1][c + 1])
print(max(sums)[0])

