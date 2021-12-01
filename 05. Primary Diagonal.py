import sys
from io import StringIO
t1 = '''3
11 2 4
4 5 6
10 8 -12
'''
t2 = '''3
1 2 3
4 5 6
7 8 9
'''
# sys.stdin = StringIO(t1)
sys.stdin = StringIO(t2)


def read_matrix():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix


matrix = read_matrix()
diagonal = [matrix[i][i] for i in range(len(matrix))]
print(sum(diagonal))
# diagonal = 0
# for r in range(len(matrix)):
#     for c in range(len(matrix[0])):
#         if r == c:
#             diagonal += matrix[r][c]
# print(diagonal)