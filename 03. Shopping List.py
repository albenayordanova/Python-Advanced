import math


def shopping_list(budget, **kwargs):
    budget = budget
    basket = set()
    for name in kwargs:
        price = float(kwargs[name][0]) * float(kwargs[name][1])
        price = math.ceil(price)
        if budget > price and len(basket) < 5:
            budget -= price
            basket.add(name)
            return f'You bought {name} for {price} leva.'

    if not basket:
        return f"You do not have enough budget...........{price}"




# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))




# def age_assignment(*args, **kwargs):
#     # result = {}
#     # for name in args:
#     #     first_letter = name[0]
#     #     result[name] = kwargs[first_letter]
#     # return result
#     return {x: kwargs[x[0]] for x in args}