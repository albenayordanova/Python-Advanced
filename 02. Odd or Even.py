cmd = input()
nums = [int(x) for x in input().split()]
parity = 0 if cmd == 'Even' else 1
print(sum(filter(lambda x: x % 2 == parity, nums)) * len(nums))