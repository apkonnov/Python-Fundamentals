with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
    result = []
    for line in file_1:
        str_1 = line.split()
        result.append((str_1[0], str_1[5][1:], str_1[6]))
    print(*result, sep=',\n')
