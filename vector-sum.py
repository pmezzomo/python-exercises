# Reads two lists of 15 numbers and creates a third list with the element-wise sum of both

list_a = []
list_b = []
list_c = []

for i in range(15):
    value = int(input("Enter a number for list A: "))
    list_a.append(value)

for i in range(15):
    value = int(input("Enter a number for list B: "))
    list_b.append(value)

for i in range(15):
    list_c.append(list_a[i] + list_b[i])

print("List A:", list_a)
print("List B:", list_b)
print("List C (A + B):", list_c)
