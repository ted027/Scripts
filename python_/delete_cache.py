import os
import shutil
import glob

def find_cache_dirs(directory):
    ls = []
    for root, dirs, files in os.walk(directory):
        for dr in dirs:
            print(f'dir: {dr}')
            if '__pycache__' in dr:
                ls.append(os.path.join(root, dr))
            elif '.pytest_cache' in dr:
                ls.append(os.path.join(root, dr))
    return ls

dir_list = find_cache_dirs('.')
print(f'dir_list: {dir_list}')


for dr in dir_list:
    print(f'remove {dr}')
    os.rmdir(dr)
