def intersection(arr1, arr2):
    result = []
    for el in arr1:
        if el in arr2:
            result.append(el)
    return result


n, m = input().split()
a = {input() for _ in range(int(n))}
b = {input() for _ in range(int(m))}

# [print(x) for x in a.intersection(b)]
[print(x) for x in intersection(a, b)]
