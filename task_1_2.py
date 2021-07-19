num_cub = []  # список, состоящий из кубов нечётных чисел от 1 до 1000
idx = 1
while idx < 1000:
    num_cub.append(idx ** 3)
    idx += 2
sum_cub = 0  # сумма чисел для пункта a задания
sum_cub17 = 0  # сумма чисел для пункта b задания
for num in num_cub:
    sum_num = 0  # сумма цифр числа из списка
    for pos_dig in range(9):  # pos_dig - позиция цифры в числе
        sum_num += num // 10 ** pos_dig % 10
    if sum_num % 7 == 0:
        sum_cub += num
    num17 = num + 17
    sum_num = 0  # сумма цифр числа из измененного списка
    for pos_dig in range(9):
        sum_num += num17 // 10 ** pos_dig % 10
    if sum_num % 7 == 0:
        sum_cub17 += num17
print('список, состоящий из кубов нечётных чисел от 1 до 1000')
print(num_cub[0:5], ' ... ', num_cub[len(num_cub)-5:len(num_cub)])
print('a) сумма чисел =', sum_cub)
print('b) сумма чисел =', sum_cub17)