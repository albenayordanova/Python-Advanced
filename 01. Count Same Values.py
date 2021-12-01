# data = [float(x) for x in input().split()]
data = tuple(map(float, input().split()))
nums = {}
for el in data:
    if el not in nums:
        nums[el] = 0
    nums[el] += 1
# print(nums)
for n, count in nums.items():
    print(f'{n:.1f} - {count} times')

# sorted_nums_by_counter = sorted((value, key) for key, value in nums.items())
# print(sorted_nums_by_counter)