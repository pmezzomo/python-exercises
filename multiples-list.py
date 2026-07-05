# Reads 10 numbers into a list, then counts and displays how many are multiples of a given divisor

def read_numbers():
    numbers = []
    multiples_count = 0

    for i in range(10):
        n = int(input("Enter a number: "))
        numbers.append(n)

    divisor = int(input("Enter the divisor: "))

    for number in numbers:
        if number % divisor == 0:
            multiples_count += 1

    print(f"Multiples of {divisor} in the list: {multiples_count}")


read_numbers()
