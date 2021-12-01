def is_valid_position(size, r, c):
    return 0 <= r < size and 0 <= c < size


def get_next_position(direction, r, c):
    if direction == 'up':
        return r - 1, c
    if direction == 'down':
        return r + 1, c
    if direction == 'left':
        return r, c - 1
    if direction == 'right':
        return r, c + 1


size = int(input())
matrix = []
alice_row, alice_col = 0, 0
for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'A':
            alice_row, alice_col = row, col
# print(alice_row, alice_col)
matrix[alice_row][alice_col] = '*'
tea = 0
while True:
    cmd = input()
    alice_row, alice_col = get_next_position(cmd, alice_row, alice_col)
    if not is_valid_position(size, alice_row, alice_col):
        break
    cell_value = matrix[alice_row][alice_col]
    matrix[alice_row][alice_col] = '*'
    if cell_value == 'R':
        break
    if cell_value.isdigit():
        tea += int(cell_value)
        if tea >= 10:
            break
if tea >= 10:
    print('She did it! She went to the party.')
else:
    print('Alice didn\'t make it to the tea party.')
for row in matrix:
    print(' '.join(row))