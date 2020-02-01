'''
    This Code is used for combine several txt files into one
'''

import os

def combine(fdir,outfile):
    file_list = os.listdir(fdir)
    file_to_write = file(outfile,'w')
    for f in file_list:
        if str(f) == 'combine.py':
            continue
        file_to_read = file(fdir+str(f),'r')
        #file_to_write.write(str(f)+'\n')  #add the file name
        while True:
            line = file_to_read.readline();
            if len(line) == 0:
                break
            else:  
                file_to_write.write(line)
        file_to_read.close()

    file_to_write.close()

if __name__ == '__main__':
    combine('./','out.txt') #fdir must end with '/'
