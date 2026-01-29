def f1(n):
    if n <= 0:
        return 0
    # check if n is power of 2 (only one set bit)
    if (n & (n - 1)) != 0:
        return 0

    # count right shifts
    c = 0
    temp = n
    while temp > 1:
        temp = temp >> 1
        c += 1

    # power of 4 -> even number of shifts
    if c % 2 == 0:
        return 1
    else:
        return 0


n = int(input("Enter a number: "))

if f1(n):
    print(n, "is a power of 4")
else:
    print(n, "is NOT a power of 4")
