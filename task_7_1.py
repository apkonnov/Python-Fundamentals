import os
conf_dict = {'my_project': {'settings': [], 'mainapp': [], 'adminapp': [], 'authapp': []}}


def make_dirs_files(root_folder, mk_dict):
    for key, val in mk_dict.items():
        if type(val) == list:
            folder = os.path.join(root_folder, key)
            os.mkdir(folder)
            for name in val:
                if type(name) == dict:
                    make_dirs_files(folder, name)
                else:
                    with open(os.path.join(folder, name), 'w', encoding='utf-8') as f:
                        pass


try:
    conf = conf_dict.popitem()
    os.mkdir(conf[0])
    make_dirs_files(conf[0], conf[1])
    print('Папка для проекта создана')
except Exception as e:
    print(f'Еrr: {e}')
