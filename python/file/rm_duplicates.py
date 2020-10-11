import os
import glob
import filecmp
 
dir_path = '.'
 
file_lst = []
 
for path in glob.glob(dir_path + '/**/*', recursive=True):
    if os.path.isfile(path):
        file_lst.append(path)
 
for x in file_lst:
    for y in file_lst:
        if x != y and os.path.exists(x) and os.path.exists(y):
            if filecmp.cmp(x, y):
                os.remove(y)
                print('removed ' + y)
