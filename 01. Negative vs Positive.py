numbers = [int(x) for x in input().split()]
pos = sum([x for x in numbers if x > 0])
neg = sum(filter(lambda x: x < 0, numbers))

print(neg)
print(pos)

if abs(neg) > pos:
    print('The negatives are stronger than the positives')
else:
    print('The positives are stronger than the negatives')