def thesaurus_adv(*args):
    names_adv = {}  # основной словарь
    list_args = list(args)  # список аргументов
    list_args.sort()
    list_key = []  # список ключей словаря
    for name in list_args:
        list_key.append(name[name.index(' ')+1])
    list_key = list(set(list_key))
    list_key.sort()

    for key in list_key:
        names = {}  # вложенный словарь
        for name in list_args:
            list_args_adv = list(filter(lambda n: n[0] == name[0] and n[n.index(' ')+1] == key, list_args))
            if list_args_adv:
                names.setdefault(name[0], list_args_adv)
        names_adv.setdefault(key, names)
    return names_adv


dict_names = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(dict_names)
