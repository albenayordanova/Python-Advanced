def is_invalid_position(row, col, size):
    if row < 0 or col < 0 or row >= size or col >= size:
        return True
    return False


def get_next_position(direction, r, c, steps):
    if direction == 'up':
        return r - steps, c
    if direction == 'down':
        return r + steps, c
    if direction == 'left':
        return r, c - steps
    return r, c + steps


size = 5
matrix = []
player_row, player_col = 0, 0
targets_count = 0
for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'A':
            player_row, player_col = row, col
        elif matrix[row][col] == 'x':
            targets_count += 1
# print(player_row, player_col)
args = int(input())
hit_targets = []
for _ in range(args):
    line = input().split()
    cmd = line[0]
    direction = line[1]
    if cmd == 'move':
        steps = int(line[2])
        next_player_row, next_player_col = get_next_position(direction, player_row, player_col, steps)
        if is_invalid_position(next_player_row, next_player_col, size):
            continue
        if matrix[next_player_row][next_player_col] != '.':
            continue
        matrix[player_row][player_col] = '.'
        matrix[next_player_row][next_player_col] = 'A'
        player_row, player_col = next_player_row, next_player_col
    else:
        bullet_row, bullet_col = get_next_position(direction, player_row, player_col, 1)
        while True:
            if is_invalid_position(bullet_row, bullet_col, size):
                break
            if matrix[bullet_row][bullet_col] == 'x':
                hit_targets.append([bullet_row, bullet_col])
                matrix[bullet_row][bullet_col] = '.'
                break

            bullet_row, bullet_col = get_next_position(direction, bullet_row, bullet_col, 1)
        if len(hit_targets) == targets_count:
            break
if len(hit_targets) == targets_count:
    print(f'Training completed! All {targets_count} targets hit.')
else:
    print(f'Training not completed! {targets_count - len(hit_targets)} targets left.')
for target in hit_targets:
    print(target)