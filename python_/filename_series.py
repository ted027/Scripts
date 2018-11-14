import os
import sys
import shutil
import glob

args = sys.argv

if len(args) < 3 or 4 < len(args):
    print(f'usage: ${args[0]} directory series-filename [connect-symbol] ')
    return

directory = args[1]
if ! os.path.exists(directory):
    print('path not found')
    return

]filename = args[2]

bef_symbol = ''
if len(args) > 3:
    bef_symbol = args[3]

aft_symbol = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
aft_symbol = aft_symbol.get(bef_symbol, '')

path = os.path.dirname(os.path.abspath(__file__))
os.mkdir(directory + "/_backup")
files = glob.glob(directory)
for i in len(files):
    shutil.copy2(files[i], os.path.join(path + '_backup/', os.path.basename(files[i])))
    basename = os.path.basename(files[i])
    full_filename = filename + bef_symbol + i + aft_symbol + os.path.splittext(basename)[1]
    os.rename(files[i], os.path.join(path, filename))


