import os


def del_emp_dir(path):
    for (root, dirs, files) in os.walk(path):
        for item in dirs:
            dir = os.path.join(root, item)
            try:
                os.rmdir(dir)
                print('remove ' + dir)
            except Exception:
                pass


if __name__ == '__main__':
    dir = '.'
    del_emp_dir(dir)
