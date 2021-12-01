size = int(input())
matrix = []
for row in range(size):
    matrix.append([int(x) for x in input().split()])
# prim = []
# sec = []
prim = 0
sec = 0
for r in range(size):
    # prim.append(matrix[r][r])
    # sec.append(matrix[r][size - r - 1])
    prim += matrix[r][r]
    sec += matrix[r][size - r - 1]
# print(abs(sum(prim) - sum(sec)))
print(abs(prim - sec))