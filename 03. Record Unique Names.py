n = int(input())
# names = set()
# for _ in range(n):
#     names.add(input())
# for el in names:
#     print(el)
names = {input() for _ in range(n)}
[print(name) for name in names]