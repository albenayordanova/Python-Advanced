# txt = input()
# stack = []
# balanced = True
# pairs = {'(': ')', '[': ']', '{': '}'}
# for ch in txt:
#     if ch in '{[(':
#         stack.append(ch)
#     else:
#         if len(stack) == 0:
#             balanced = False
#             break
#         last_opening_bracket = stack.pop()
#         if pairs[last_opening_bracket] != ch:
#             balanced = False
#             break
# if balanced and len(stack) == 0:
#     print('YES')
# else:
#     print('NO')

# txt = input()
# opening = []
# balanced = True
# for el in txt:
#     if el in '({[':
#         opening.append(el)
#     else:
#         if not opening:
#             balanced = False
#             break
#         last_opening = opening.pop()
#         pair = f'{last_opening}{el}'
#         if pair not in '(){}[]':
#             balanced = False
#             break
#
# if balanced and not opening:
#     print('YES')
# else:
#     print('NO')

expression = input()
balanced = True
stack = []
for paren in expression:
    if paren in '({[':
        stack.append(paren)
    elif paren in ')}]':
        if len(stack) == 0:
            balanced = False
            break
        opening_paren = stack.pop()
        if f'{opening_paren}{paren}' not in ['{}', '()', '[]']:
            balanced = False
            break
if balanced and len(stack) == 0:
    print('YES')
else:
    print('NO')