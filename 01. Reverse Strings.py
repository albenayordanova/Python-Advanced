txt = input()
ss = []
for el in txt:
    ss.append(el)
result = ''
while ss:
    result += ss.pop()
print(result)
