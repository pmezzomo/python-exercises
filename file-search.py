# Searches for a word in a text file and reports whether it was found

search = input("Enter a word to search: ")

with open('test.txt', 'r') as f:
    lines = f.readlines()

found = any(search in line for line in lines)

if found:
    print("Word found in the file.")
else:
    print("Word not found in the file.")
