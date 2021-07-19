for num in range(21):
    if num // 10 % 10 == 1: # первый десяток
        print(num, 'процентов')
    elif num % 10 == 1: # последняя цифра 1
        print(num, 'процент')
    elif 1 < num % 10 < 5: # последняя цифра 2,3,4
        print(num, 'процента')
    else:
        print(num, 'процентов')