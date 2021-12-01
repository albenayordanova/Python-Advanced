def permute(index, values):
    if index == len(values):
        print(''.join(values))
        return
    for i in range(index, len(values)):
        values[i], values[index] = values[index], values[i]
        permute(index + 1, values)
        values[i], values[index] = values[index], values[i]


permute(0, list(input()))

# def perm(txt, ind):
#     if ind >= len(txt):
#         print(''.join(txt))
#         return
#     perm(txt, ind + 1)
#     for i in range(ind + 1, len(txt)):
#         txt[ind], txt[i] = txt[i], txt[ind]
#         perm(txt, ind + 1)
#         txt[ind], txt[i] = txt[i], txt[ind]
#
#
# data = list(input())
# perm(data, 0)