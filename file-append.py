# Demonstrates appending lines to a file across multiple steps and overwriting from the beginning

def step1():
    # Creates (or appends to) the file and writes 3 lines
    with open('new.txt', 'a+') as f:
        f.write('Line 1\n')
        f.write('Line 2\n')
        f.write('Line 3\n')


def step2():
    # Appends a 4th line to the existing file
    with open('new.txt', 'a+') as f:
        f.write('Line 4\n')


def step3():
    # Opens in r+ mode: writes from the beginning, overwriting existing content
    with open('new.txt', 'r+') as f:
        f.write('Line 99\n')


# step1()
# step2()
step3()
