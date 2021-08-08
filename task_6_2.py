with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
    spam = {}
    for line in file_1:
        str_1 = line.split()
        key = str_1[0]
        val = spam.setdefault(key, 0)
        spam[key] = val + 1
    max_val = max(spam.values())
    spammer = {key: val for key, val in spam.items() if val == max_val}
    print(spammer)
