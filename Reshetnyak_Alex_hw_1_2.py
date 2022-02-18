odd_numbers = list(range(1, 1000, 2))
pow_odd_numbers = []
number = 0
for i in odd_numbers:
    el = i ** 3
    pow_odd_numbers.append(el)
    i += 1
#     while el != 0 in pow_odd_numbers:
#         number += el % 10
#         el //= 10
# print(number)
    for e in pow_odd_numbers:
        # while e > 0:
        dig = e % 10
        number = number + dig
        e = e // 10
        if number % 7 == 0:
            num = 0
            num = num + number
            print(num)
