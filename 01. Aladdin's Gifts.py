from collections import deque

boxes = [int(x) for x in input().split()]
magics = deque([int(x) for x in input().split()])
ttl = {}


while boxes and magics:
    current_box = boxes.pop()
    current_magic = magics.popleft()
    craft = current_box + current_magic
    if craft < 100:
        if craft % 2 == 0:
            craft = current_box * 2 + current_magic * 3
        else:
            craft = (current_box + current_magic) * 2
    elif craft > 499:
    # if craft > 499:
        craft = (current_box + current_magic) / 2
    if 99 < craft < 500:

        if 99 < craft < 200:
            name = 'Gemstone'
            if name not in ttl:
                ttl[name] = 0
            ttl[name] += 1
        elif 199 < craft < 300:
            name = 'Porcelain Sculpture'
            if name not in ttl:
                ttl[name] = 0
            ttl[name] += 1
        elif 299 < craft < 400:
            name = 'Gold'
            if name not in ttl:
                ttl[name] = 0
            ttl[name] += 1
        elif 399 < craft < 500:
            name = 'Diamond Jewellery'
            if name not in ttl:
                ttl[name] = 0
            ttl[name] += 1

is_done = ('Gemstone' in ttl and 'Porcelain Sculpture' in ttl) or ('Gold' in ttl and 'Diamond Jewellery' in ttl)

if is_done:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if boxes:
    print(f'Materials left: {", ".join(reversed([str(x) for x in boxes]))}')
if magics:
    print(f'Magic left: {", ".join([str(x) for x in magics])}')
for k, v in sorted(ttl.items()):
    print(f'{k}: {v}')
