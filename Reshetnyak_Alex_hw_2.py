odd_numbers = list(range(1, 1000, 2))
pow_odd_numbers = []
for i in odd_numbers:
    el = i ** 3
    pow_odd_numbers.append(el)
    i += 1
print(pow_odd_numbers)

"""Вариант без нового списка"""
odd_numbers = list(range(1, 1000, 2))
pow_odd_numbers = []
for i in odd_numbers:
    el = i ** 3
    pow_odd_numbers.append(el)
    i += 1
print(pow_odd_numbers)
