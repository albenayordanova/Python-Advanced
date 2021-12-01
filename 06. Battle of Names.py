n = int(input())
even_nums = set()
odd_nums = set()
for i in range(1, n + 1):
    name = input()
    # ttl = 0
    # for el in name:
    #     ttl += ord(el)
    # ttl //= i
    ttl = sum([ord(x) for x in name]) // i
    if ttl % 2 == 0:
        even_nums.add(ttl)
    else:
        odd_nums.add(ttl)

result = set()
if sum(even_nums) == sum(odd_nums):
    result = odd_nums.union(even_nums)

elif sum(even_nums) < sum(odd_nums):
    result = odd_nums.difference(even_nums)

else:
    result = odd_nums.symmetric_difference(even_nums)

print(', '.join(str(x) for x in result))