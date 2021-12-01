def comb(txt, index, count, combination):
    if len(combination) == count:
        print(', '.join(combination))
        return
    for i in range(index, len(txt)):
        combination.append(txt[i])
        comb(txt, i + 1, count, combination)
        combination.pop()


names = input().split(', ')
n = int(input())
comb(names, 0, n, [])