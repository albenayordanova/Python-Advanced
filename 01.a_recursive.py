n = 6
index = 0
# while True:
#     if index == n:
#         break
#     print(index)
#     index += 1


def f1(index, n):
    if index == n:
        return
    print(index)
    f1(index=index + 1, n=n)


f1(index=0, n=n)