# n = int(input())
# guests = set()
# for _ in range(n):
#     guests.add(input())
# cmd = input()
# while not cmd == "END":
#     guests.remove(cmd)
#     cmd = input()
# print(len(guests))
# vip = [el for el in guests if el[0].isdigit()]
# reg = [el for el in guests if not el[0].isdigit()]
# [print(car) for car in sorted(vip)]
# [print(car) for car in sorted(reg)]

n = int(input())
guests = {input() for _ in range(n)}
while True:
    cmd = input()
    if cmd == 'END':
        break
    guests.remove(cmd)


def is_vip(name):
    return name[0].isdigit()


print(len(guests))
vip = sorted([g for g in guests if is_vip(g)])
reg = sorted([g for g in guests if not is_vip(g)])
[print(car) for car in vip]
[print(car) for car in reg]