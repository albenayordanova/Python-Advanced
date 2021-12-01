 def is_inside(row_size, col_size, r, c):
    return 0 <= r < row_size and 0 <= c < col_size


def get_next_position(direction, r, c):
    if direction == 'L':
        return r, c - 1
    if direction == 'R':
        return r, c + 1
    if direction == 'U':
        return r - 1, c
    if direction == 'D':
        return r + 1, c


def get_bunnies_in_range(bunnies, x, y):
    next_bunnies = []
    for r, c in bunnies:
        if is_inside(x, y, r - 1, c):
            next_bunnies.append([r - 1, c])
        if is_inside(x, y, r + 1, c):
            next_bunnies.append([r + 1, c])
        if is_inside(x, y, r, c - 1):
            next_bunnies.append([r, c - 1])
        if is_inside(x, y, r, c + 1):
            next_bunnies.append([r, c + 1])
    return next_bunnies


n, m = [int(x) for x in input().split()]
matrix = []
player_row, player_col = 0, 0
bunnies = []
for row in range(n):
    matrix.append(list(input()))
    for col in range(m):
        if matrix[row][col] == 'P':
            player_row, player_col = row, col
        elif matrix[row][col] == 'B':
            bunnies.append([row, col])
matrix[player_row][player_col] = '.'
won = None
line = input()
for el in line:
    next_player_row, next_player_col = get_next_position(el, player_row, player_col)
    if not is_inside(n, m, next_player_row, next_player_col):
        won = True
    elif matrix[next_player_row][next_player_col] == 'B':
        won = False
    if not won:
        player_row, player_col = next_player_row, next_player_col
    next_bunnies = get_bunnies_in_range(bunnies, n, m)
    for row, col in next_bunnies:
        if row == player_row and col == player_col and not won:
            won = False
        matrix[row][col] = 'B'
    bunnies += next_bunnies

    if won is not None:
        break

for el in matrix:
    print(''.join(el))
if won:
    print(f'won: {player_row} {player_col}')
else:
    print(f'dead: {player_row} {player_col}')

# 7 3
# ...
# .B.
# .P.
# ...
# ...
# ...
# ...
# DDDDDDD