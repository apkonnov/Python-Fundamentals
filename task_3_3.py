def thesaurus(*args):
    names = {}
    list_args = list(args)
    list_args.sort()
    for name in list_args:
        names.setdefault(name[0], list(filter(lambda n: n[0] == name[0], list_args)))
    return names


dict_names = thesaurus("Петр", "Иван", "Мария", "Илья")
print(dict_names)
