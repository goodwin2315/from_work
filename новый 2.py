# count = 1
# while count >= 100:
#     n1 = 'процент'
#     n2 = 'процента'
#     n3 = 'процентов'
#     if 10 <= count % 100 <= 20:
#         print(count, n3)
#     elif count % 10 == 1:
#         print(count, n1)
#     elif 2 <= count % 10 <= 4:
#         print(count, n2)
#     else:
#         print(count, n1)
#     count += 1


def sum_digits(value):
    res = 0

    while value != 0:
        res += value % 10
        value //= 10

    return res


arr = [i**3 for i in range(1, 1001, 2)]

res1 = sum(filter(lambda num: sum_digits(num) % 7 == 0, arr))
res2 = sum(filter(lambda num: sum_digits(num + 17) % 7 == 0, arr))

print(res1)
print(res2)