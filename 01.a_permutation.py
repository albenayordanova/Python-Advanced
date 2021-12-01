def perm(txt, ind):
    if ind >= len(txt):
        print(''.join(txt))
        return
    perm(txt, ind + 1)
    for i in range(ind + 1, len(txt)):
        txt[ind], txt[i] = txt[i], txt[ind]
        perm(txt, ind + 1)
        txt[ind], txt[i] = txt[i], txt[ind]


data = list(input())
perm(data, 0)