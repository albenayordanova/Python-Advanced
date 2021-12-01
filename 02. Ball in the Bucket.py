matrix = []
buckets = []
for row in range(6):
    matrix.append([x for x in input().split()])
# print(matrix)
ttl = 0
trows = []
for trow in range(3):
    r1, c1 = [x for x in input().split(', ')]
    r = int(r1[1:])
    c = int(c1[:-1])
    # print(c)
    if 0 <= r < 6 and 0 <= c < 6 and matrix[r][c] == 'B':
        if (r, c) not in buckets:
            buckets.append((r, c))
            for row in range(6):
                if not matrix[row][c] == 'B':
                    ttl += int(matrix[row][c])
        else:
            continue
if ttl < 100:
    print(f"Sorry! You need {100 - ttl} points more to win a prize.")
elif 99 < ttl < 200:
    print(f'Good job! You scored {ttl} points, and you\'ve won Football.')
elif 199 < ttl < 300:
    print(f'Good job! You scored {ttl} points, and you\'ve won Teddy Bear.')
elif ttl >= 300:
    print(f'Good job! You scored {ttl} points, and you\'ve won Lego Construction Set.')
# print(buckets)