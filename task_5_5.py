src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_src = set()
tmp = set()
for el in src:
    if el not in tmp:
        unique_src.add(el)
    else:
        unique_src.discard(el)
    tmp.add(el)
result = [el for el in src if el in unique_src]
print(result)
