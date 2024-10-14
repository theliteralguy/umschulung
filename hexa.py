def hexa(num):
    hex_digits = '0123456789ABCDEF'
    remainders = []
    while num > 0:
        remainder = num % 16
        num = num // 16
        remainders.append(remainder)
        hexadecimal = ""
    print(remainders)


print(hexa(12345))

