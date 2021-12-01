n, m = [int(x) for x in input().split()]
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split()])
# sums = []
max_sum, best_r, best_c = 0, 0, 0
for r in range(n - 2):
    for c in range(m - 2):
        current_sum = matrix[r][c] + matrix[r][c + 1] + matrix[r][c + 2] \
                      + matrix[r + 1][c] + matrix[r + 1][c + 1] + matrix[r + 1][c + 2] \
                      + matrix[r + 2][c] + matrix[r + 2][c + 1] + matrix[r + 2][c + 2]
        # row, col = r, c
        # sums.append((current_sum, row, col))
        if current_sum > max_sum:
            max_sum, best_r, best_c = current_sum, r, c
print(f'Sum = {max_sum}')
best_r = r
best_c = c
# max_sum = max(sums)
# print(sums)
# print(f'Sum = {max_sum[0]}')
# r = max_sum[1]
# c = max_sum[2]
print(matrix[r][c], matrix[r][c + 1], matrix[r][c + 2])
print(matrix[r + 1][c], matrix[r + 1][c + 1], matrix[r + 1][c + 2])
print(matrix[r + 2][c], matrix[r + 2][c + 1], matrix[r + 2][c + 2])