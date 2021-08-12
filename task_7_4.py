import os
import django

root_dir = django.__path__[0]
django_size = {100: 0, 1000: 0, 10000: 0, 100000: 0, 1000000: 0, 10000000: 0}
for root, dirs, files in os.walk(root_dir):
    for file in files:
        file_size = os.stat(os.path.join(root, file)).st_size
        key = 10 ** len(str(file_size))
        if key < 100:
            key = 100
        django_size[key] += 1
print(django_size)
