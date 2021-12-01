import sys
from io import StringIO

test_1 = '''3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0
'''
test_2 = '''3, 3
1 2 3
4 5 6
7 8 9
'''
# sys.stdin = StringIO(test_1)
sys.stdin = StringIO(test_2)


def read_matrix():
    n, m = [int(x) for x in input().split(', ')]
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix


matrix = read_matrix()
n = len(matrix)
m = len(matrix[0])
columns_sum = [0] * m
for row in range(n):
    for column in range(m):
        value = matrix[row][column]
        columns_sum[column] += value

[print(x) for x in columns_sum]

# for column in range(m):
#     ttl = 0
#     for row in range(n):
#         ttl += matrix[row][column]
#     print(ttl)

