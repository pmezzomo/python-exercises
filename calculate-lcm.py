# Calculates the Least Common Multiple (LCM) of three integers using successive prime division

def calculate_lcm(n1, n2, n3):
    lcm = 1
    divisor = 2
    message = "LCM(%d, %d, %d) = " % (n1, n2, n3)

    while not (n1 == 1 and n2 == 1 and n3 == 1):
        has_divisor = False

        if n1 % divisor == 0:
            n1 = n1 // divisor
            has_divisor = True
        if n2 % divisor == 0:
            n2 = n2 // divisor
            has_divisor = True
        if n3 % divisor == 0:
            n3 = n3 // divisor
            has_divisor = True

        if has_divisor:
            lcm = lcm * divisor
        else:
            divisor += 1

    print(message, lcm)

calculate_lcm(12, 15, 18)
calculate_lcm(11, 15, 18)
