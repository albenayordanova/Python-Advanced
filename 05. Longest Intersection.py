n = int(input())
longest = []
for _ in range(n):
    temp = []
    a = set()
    b = set()
    a12, b12 = input().split('-')
    a1, a2 = a12.split(',')
    b1, b2 = b12.split(',')
    for i in range(int(a1), int(a2) + 1):
        a.add(i)
    for i in range(int(b1), int(b2) + 1):
        b.add(i)
    temp = a & b
    if len(longest) < len(temp):
        longest = temp

print(f'Longest intersection is [{", ".join(str(x) for x in longest)}] with length {len(longest)}')