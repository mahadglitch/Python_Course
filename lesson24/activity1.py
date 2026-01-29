def is_power_of_2(n):
    if n <= 0:
        return False

    # only one set bit for powers of 2
    return (n & (n - 1)) == 0


n = int(input("Enter a number: "))

if is_power_of_2(n):
    print(n, "is a power of 2 🔥")
else:
    print(n, "is NOT a power of 2 ❌")
