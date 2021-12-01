n = int(input())
cars = set()
for _ in range(n):
    cmd, name = input().split(', ')
    if cmd == 'IN':
        cars.add(name)
    elif cmd == 'OUT':
        cars.remove(name)
if cars:
    [print(car) for car in cars]
else:
    print('Parking Lot is Empty')