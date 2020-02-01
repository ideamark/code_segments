'''
    This Code is used for split one txt into several pieces
'''


fileName = 'all'
lines_per_file = 100

def split(fName):
    file_to_read = file(fName,'r')
    Lines = file_to_read.readlines()
    max_lines = len(Lines)
    count = 0
    file_count = 1
    file_to_write = file(str(file_count),'w')
    for line in Lines:
        file_to_write.write(line)
        count += 1
        if count % lines_per_file == 0 and count < max_lines:
            file_to_write.close()
            file_count += 1
            file_to_write = file(str(file_count),'w')
    file_to_read.close()
    file_to_write.close()

if __name__ == '__main__':
    split(fileName)
