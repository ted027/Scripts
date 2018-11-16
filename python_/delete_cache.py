import os
import shutil
import glob

file_list = glob.glob('./*__pycache__*') + glob.glob('./*.pytest_cache*')
print(f'file_list: {file_list}')

dir_list = list(set([os.path.dirname(fil) for fil in file_list]))
print(f'dir_list: {dir_list}')

for dr in dir_list:
    print(f'remopve {dr}')
    shutil.rmtree(dr, ignore_errors=True)
