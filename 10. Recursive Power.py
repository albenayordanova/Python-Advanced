# def recursive_power(number, power):
#     result = number
#     for _ in range(power - 1):
#         result *= number
#     return result


def recursive_power(base, exponent):
    if exponent == 1:
        return base
    return base * recursive_power(base, exponent - 1)