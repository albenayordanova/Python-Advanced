ll = [1, 2, 3, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5]
target = 9
c = 0
n = len(ll)
for i in range(n):
    for j in range(i + 1, n):
        c += 1
        if i == j:
            continue
        if ll[i] + ll[j] == target:
            print(ll[i], ll[j])
# remains = set()
# for x in ll:
#     c += 1
#     if x in remains:
#         print(x)
#     remains.add(target - x)
print(f'Iterations: {c}')