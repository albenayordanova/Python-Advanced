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
# sys.stdin = StringIO(t1)
sys.stdin = StringIO(t2)


def read_matrix():
    n, m = [int(x) for x in input().split(', ')]
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
    return matrix


matrix = read_matrix()

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix[i][j] += 1
print(matrix)