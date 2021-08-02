def power2(x, n):
    if n == 0:
        return 1
    return x * power2(x, n - 1)


# print(power2(2,3))

# EXTENSION TO_DO
# def power3(x, n):
#     if n == 0:
#         return 1
#     return  x * power3(x * x, n / 2)
