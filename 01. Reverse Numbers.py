nums = input().split()
rev = []
while nums:
    el = nums.pop()
    rev.append(el)
    # rev.append(nums.pop())
print(' '.join(rev))

# data = input().split()
# while data:
#     x = data.pop()
#     if data:
#         print(x, end=' ')
#     else:
#         print(x)