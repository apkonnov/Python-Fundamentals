n = int(input('n = '))
odd_to_n = (num for num in range(1, n + 1, 2))
print(*odd_to_n, sep=', ')
