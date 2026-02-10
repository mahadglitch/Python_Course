def is_power_of_8(n):
    if n <= 0:
        return False

    # divide by 8 until you can't
    while n % 8 == 0:
        n //= 8

    return n == 1


num = int(input("Enter a number: "))

if is_power_of_8(num):
    print(num, "is a power of 8 🔥")
else:
    print(num, "is NOT a power of 8 ❌")
