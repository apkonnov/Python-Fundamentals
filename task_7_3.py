import os
import shutil

#  root = r'c:\Users\konno_xt\PycharmProjects\python_gb\my_project'
root_dir = os.path.abspath('my_project')
_dir = os.path.join(root_dir, 'templates')
from_dir = []
to_dir = []
for root, dirs, files in os.walk(root_dir):
    if 'templates\\' in root:
        from_dir.append(root)
        to_dir.append(os.path.join(_dir, str(root.split('\\')[-1])))

try:
    os.mkdir(_dir)
    for i in range(len(from_dir)):
        shutil.copytree(from_dir[i], to_dir[i])
except Exception as e:
    print(f'Err: {e}')
