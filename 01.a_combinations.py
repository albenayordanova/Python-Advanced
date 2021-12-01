def combination(values, index, count, comb):
    if len(comb) == count:
        print(comb)
        return
    for i in range(index, len(values)):
        comb.append(values[i])
        combination(values, i + 1, count, comb)
        comb.pop()


# combination(['p', 'g', 'a'], 0, 2, [])
# combination(['p', 'g', 'a', 'x'], 0, 3, [])
data = input()
combination(list(data), 0, len(data) - 1, [])