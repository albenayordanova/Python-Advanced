line = input().split('|')
result = []
for el in range(len(line) - 1, -1, -1):
    temp = line[el].split()
    result += temp
print(' '.join(result))