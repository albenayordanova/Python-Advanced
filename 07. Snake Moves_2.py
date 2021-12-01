rows, cols = [int(x) for x in input().split()]
word = input()
matrix = []
word_idx = 0
for row in range(rows):
    matrix.append([None] * cols)
    for col in range(cols):
        col_idx = col if row % 2 == 0 else cols - 1 - col
        if row % 2 == 0:
            matrix[row][col_idx] = word[word_idx]
        else:
            matrix[row][col_idx] = word[word_idx]
        word_idx = (word_idx + 1) % len(word)
for element in matrix:
    print(''.join(element))