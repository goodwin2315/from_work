odd_numbers = list(range(1, 1000, 2))
pow_odd_numbers = []
number = 0
for i in odd_numbers:
    el = i ** 3
    pow_odd_numbers.append(el)
    i += 1
for el in pow_odd_numbers:
    my_list = []
    while el > 0:
        number = number + el % 10
        el = el // 10
        pow_odd_numbers.append(number)
print(pow_odd_numbers)
