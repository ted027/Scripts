import sys, os
import glob

os.makedirs('./converted', exist_ok=True)
filepathlist = glob.glob('./*.json')

for path in filepathlist:
    split_path = os.path.splitext(path)[0] + '.properties'
    after_basename = os.path.basename(split_path)
    after_path = './converted/' + after_basename
    with open(path) as f:
        f_str = f.read()
        f_prop = f_str.replace('{\n', '').replace('\n}', '\n').replace('    ', '').replace(
            ',\n', '\n').replace('\": \"', '=').replace('\"', '')
    
    with open(after_path, mode='w') as aft_f:
        aft_f.write(f_prop)
