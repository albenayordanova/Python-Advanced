def even_odd(*args):
    cmd = args[-1]
    result = []
    parity = 0 if cmd == 'even' else 1
    for num in args[0:len(args) - 1]:
        if num % 2 == parity:
            result.append(num)
    return result


# def even_odd(cmd, *args):
#     parity = 0 if cmd == 'even' else 1
#     return [x for x in args if x % 2 == parity]


def even_odd(*args):
    result = []
    if args[-1] == 'even':
        result = [int(x) for x in args[:-1] if int(x) % 2 == 0]
    else:
        result = [int(x) for x in args[:-1] if int(x) % 2 == 1]
    return result


