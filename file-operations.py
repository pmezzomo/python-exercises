# Demonstrates writing, appending, reading, and opening text files with different modes

def write_to_file():
    # fix: replaced Windows absolute path (c:\\teste\\) with relative path
    with open('example.txt', 'w') as f:
        f.write('Hello everyone! Good evening! How are you?')
        f.write('\nToday we will work with file manipulation.')
        f.write('\nHope you enjoy it!')


def append_to_file():
    with open('example.txt', 'a') as f:
        lines = ['\nNew line 1', '\nNew line 2', '\nNew line 3']
        f.writelines(lines)


def read_entire_file():
    with open('example.txt', 'r') as f:
        print(f.read())


def read_line_by_line():
    with open('example.txt', 'r') as f:
        print(f.readline())


def read_all_lines():
    with open('example.txt', 'r') as f:
        lines = f.readlines()
        print('Total lines:', len(lines))
        for line in lines:
            print(line)


def open_with_context_manager():
    # 'with' ensures the file is automatically closed after the block
    with open('example.txt', 'w') as f:
        f.write('Line 1\n')
        f.write('Line 2\n')
        f.write('Line 3\n')


open_with_context_manager()
