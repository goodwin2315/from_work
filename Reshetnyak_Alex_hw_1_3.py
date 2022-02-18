n1 = 'процентов'
count = 1
while count >= 100:
    if count == 0:
        print(count + n1)
elif count % 100 >= 10 and count % 100 <= 20:
    print(str(s) + n1)
elif s%10==1:
print(str(s) + n2)
elif s%10>=2 and s%10<=4:
print(str(s) + n3)
else:
print(str(s) + n1)
