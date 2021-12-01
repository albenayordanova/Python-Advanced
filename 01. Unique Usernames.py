n = int(input())
names = {input() for _ in range(n)}
print('\n'.join(names))
# [print(name) for name in names]