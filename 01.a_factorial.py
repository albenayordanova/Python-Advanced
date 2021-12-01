def factorial(n):
    print(f'Calculating {n}')
    if n == 0 or n == 1:
        return 1
    result = n * factorial(n - 1)
    print(f'f({n})={result}')

    return result


def fac_2(n):
    if n > 1:
        result = n * factorial(n - 1)
        print(result)
    return 1


# factorial(5)
fac_2(5)