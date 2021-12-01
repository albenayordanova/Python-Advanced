def add(y, z, *args, **kwargs):
    print(y)
    print(z)
    print(args)
    print(kwargs)
    print(kwargs.values())
    print(args.count(3))
    return sum(args)


print(add(1, 2, 3, 4, a=(5, 6), b=(7, 8), c=(9, 10)))