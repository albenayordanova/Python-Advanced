def operate(operator, *args):
    result = args[0]
    for el in args[1:]:
        if operator == '+':
            result += el
        elif operator == '-':
            result -= el
        elif operator == '*':
            result *= el
        elif operator == '/':
            result /= el
    return result


print(operate('-', 3, 4))
