# Check whether the two numbers are equal or not.
n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))
if (n1 ^ n2) == 0:
    print(n1, "and", n2, "are equal numbers")
else:
    print(n1, "and", n2, "are not equal numbers")
