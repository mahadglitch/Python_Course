def reverse_bits(n, bits=8):
    rev = 0
    for i in range(bits):
        rev = (rev << 1) | (n & 1)
        n >>= 1
    return rev


# Example
num = int(input("Enter a number: "))
bits = int(input("How many bits? (e.g. 8, 16, 32): "))

result = reverse_bits(num, bits)

print("Original :", format(num, f'0{bits}b'))
print("Reversed :", format(result, f'0{bits}b'))
print("Decimal  :", result)
