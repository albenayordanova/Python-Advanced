expression = input()
stack = []
# for index, ch in enumerate(expression):
#     if ch == '(':
#         stack.append(index)
#     elif ch == ')':
#         closing = index
#         opening = stack.pop()
#         result = expression[opening:closing + 1]
#         print(result)

for i in range(len(expression)):
    if expression[i] == '(':
        stack.append(i)
    elif expression[i] == ')':
        opening = stack.pop()
        print(expression[opening:i + 1])