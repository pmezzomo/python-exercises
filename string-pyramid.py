# Reads a word and prints it as a growing pyramid, adding one letter per line

word = input("Enter a word: ")

for i in range(len(word)):
    print(word[:i + 1])  # slices from the start up to position i+1
