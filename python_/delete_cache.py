import os
import shutil
import glob

def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)

file_list = glob.glob('./*__pycache__*') + glob.glob('./*.pytest_cache*')
print(f'file_list: {file_list}')

dir_list = list(set([os.path.dirname(fil) for fil in file_list]))
print(f'dir_list: {dir_list}')

for dr in dir_list:
    print(f'remopve {dr}')
    # shutil.rmtree(dr, ignore_errors=True)
    # delete
