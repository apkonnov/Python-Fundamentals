def odd_nums(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


odd_to_n = odd_nums(int(input('n = ')))
print(*odd_to_n, sep=', ')
