number_10 = int(input())
binary = bin(number_10)
octal = oct(number_10)
hex = hex(number_10)

print(binary[2::])
print(octal[2::])
print(hex[2::].upper())
