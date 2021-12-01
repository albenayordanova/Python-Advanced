from collections import deque
boxes = [int(x) for x in input().split()]
magics = deque([int(x) for x in input().split()])
ttl = {}
presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle',
}
while boxes and magics:
    current_box = boxes.pop()
    current_magic = magics.popleft()
    craft = current_box * current_magic
    if current_magic == 0 and current_box == 0:
        continue
    if current_box == 0:
        magics.appendleft(current_magic)
        continue
    if current_magic == 0:
        boxes.append(current_box)
        continue
    if craft < 0:
        boxes.append(current_box + current_magic)
    elif craft in presents:
        gift = presents[craft]
        if gift in ttl:
            ttl[gift] += 1
        else:
            ttl[gift] = 1
    else:
        boxes.append(current_box + 15)

is_done = ('Teddy bear' in ttl and 'Bicycle' in ttl) or ('Doll' in ttl and 'Wooden train' in ttl)

if is_done:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')
if boxes:
    print(f'Materials left: {", ".join(reversed([str(x) for x in boxes]))}')
if magics:
    print(f'Materials left: {", ".join([str(x) for x in magics])}') 
for k, v in sorted(ttl.items()):
    print(f'{k}: {v}')

# 10 -5 20 15 -30 10
# 40 60 10 4 10 0