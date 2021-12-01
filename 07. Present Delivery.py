def is_valid_position(size, r, c):
    return 0 <= r < size and 0 <= c < size


def get_next_position(direction, r, c):
    if direction == 'up':
        return r - 1, c
    if direction == 'down':
        return r + 1, c
    if direction == 'left':
        return r, c - 1
    return r, c + 1


def get_houses_in_range(size, r, c):
    houses = []
    if is_valid_position(size, r - 1, c):
        houses.append([r - 1, c])
    if is_valid_position(size, r + 1, c):
        houses.append([r + 1, c])
    if is_valid_position(size, r, c - 1):
        houses.append([r, c - 1])
    if is_valid_position(size, r, c + 1):
        houses.append([r, c + 1])
    return houses


presents = int(input())
size = int(input())
matrix = []
santa_row, santa_col = 0, 0
# naughty_kid = 0
nice_kid = 0
# cookies = 0
for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'S':
            santa_row, santa_col = row, col
        # elif matrix[row][col] == 'X':
            # naughty_kid += 1
        elif matrix[row][col] == 'V':
            nice_kid += 1
        # elif matrix[row][col] == 'C':
        #     cookies += 1
# print(santa_row, santa_col)
kid = nice_kid
while True:
    line = input()
    if line == 'Christmas morning':
        break
    next_santa_row, next_santa_col = get_next_position(line, santa_row, santa_col)
    if matrix[next_santa_row][next_santa_col] == 'V':
        kid -= 1
        presents -= 1
    elif matrix[next_santa_row][next_santa_col] == 'C':
        houses_in_range = get_houses_in_range(size, next_santa_row, next_santa_col)
        for row, col in houses_in_range:
            if matrix[row][col] == 'X':
                presents -= 1
                # naughty_kid -= 1
            if matrix[row][col] == 'V':
                presents -= 1
                kid -= 1
            matrix[row][col] = '-'
            if presents == 0:
                break
    matrix[santa_row][santa_col] = '-'
    matrix[next_santa_row][next_santa_col] = 'S'
    santa_row, santa_col = next_santa_row, next_santa_col
    if presents == 0:
        break
if presents == 0 and kid > 0:
    print('Santa ran out of presents!')
for el in matrix:
    print(' '.join(el))
if kid == 0:
    print(f'Good job, Santa! {nice_kid} happy nice kid/s.')
else:
    print(f'No presents for {kid} nice kid/s.')