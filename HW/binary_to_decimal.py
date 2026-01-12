binary = input("Enter a binary number: ")

is_valid = True
for digit in binary:
    if digit not in ("0", "1"):
        is_valid = False
        break

if is_valid:
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)

    print("Decimal value:", decimal)
else:
    print("Invalid binary number! Please use only 0 and 1.")
