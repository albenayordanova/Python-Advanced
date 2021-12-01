import sys
from io import StringIO
test_input_1 = '''3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0
'''
test_input_2 = '''2, 4
10, 11, 12, 13
14, 15, 16, 17
'''
sys.stdin = StringIO(test_input_1)
# sys.stdin = StringIO(test_input_2)


def read_matrix():
    n, m = [int(x) for x in input().split(', ')]
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
    return matrix


matrix = read_matrix()
n = len(matrix)
m = len(matrix[0])
# ttl = 0
for row_index in range(n):
    row = matrix[row_index]
    # ttl += sum(row)
    # for column_index in range(m):
    #     ttl += row[column_index]
print(sum(sum(row) for row in matrix))
# print(ttl)
print(matrix)

# (n, m) = [int(x) for x in input().split(', ')]
# # n, m = map(int, input().split(', '))
# matrix = []
# ttl = 0
# for _ in range(n):
#     row = [int(x) for x in input().split(', ')]
#     ttl += sum(row)
#     matrix.append(row)
# print(ttl)
# print(matrix)