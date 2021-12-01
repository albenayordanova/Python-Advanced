f = {int(x) for x in input().split()}
s = set([int(x) for x in input().split()])
n = int(input())
for _ in range(n):
    cmd = input().split()
    act = cmd[0]
    pos = cmd[1]
    if act == 'Add' and pos == 'First':
        [f.add(int(x)) for x in cmd[2:]]
        # for el in cmd[2:]:
        #     f.add(int(el))
    elif act == 'Add' and pos == 'Second':
        [s.add(int(x)) for x in cmd[2:]]
    elif act == 'Remove' and pos == 'First':
        temp = set([int(x) for x in cmd[2:]])
        f = f.difference(temp)
        # for el in cmd[2:]:
        #     if int(el) in f:
        #         f.remove(int(el))
    elif act == 'Remove' and pos == 'Second':
        temp = set([int(x) for x in cmd[2:]])
        s = s.difference(temp)
    else:
        print(f.issubset(s) or s.issubset(f))
print(', '.join([str(x) for x in sorted(f)]))
print(', '.join([str(x) for x in sorted(s)]))