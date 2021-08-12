import os
import django
import json

root_dir = django.__path__[0]
django_size = {100: [0, []], 1000: [0, []], 10000: [0, []], 100000: [0, []], 1000000: [0, []], 10000000: [0, []]}
for root, dirs, files in os.walk(root_dir):
    for file in files:
        file_size = os.stat(os.path.join(root, file)).st_size
        key = 10 ** len(str(file_size))
        if key < 100:
            key = 100
        django_size[key][0] += 1
        django_size[key][1].append(file.rsplit('.', maxsplit=1)[-1].lower())
for key, val in django_size.items():
    val[1] = list(set(val[1]))
    django_size[key] = tuple(val)
print(django_size)

with open('summary.json', 'w', encoding='utf-8') as f:
    json.dump(django_size, f, ensure_ascii=False)
