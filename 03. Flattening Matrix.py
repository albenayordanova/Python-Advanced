import sys
from io import StringIO

test_1 = '''2
1, 2, 3
4, 5, 6
'''
test_2 = '''3
10, 2, 21, 4
5, 20, 41, 9
6, 2, 4, 99
'''
sys.stdin = StringIO(test_1)


# sys.stdin = StringIO(test_2)


def read_matrix():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
    return matrix


matrix = read_matrix()
# print([x for row in matrix for x in row])
flatt_matrix = []
for row in matrix:
    # flatt_matrix += row
    flatt_matrix.extend(row)
print(flatt_matrix)
