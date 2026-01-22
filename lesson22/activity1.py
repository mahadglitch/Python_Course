def numberOfBits(n):
    ones = 0
    zeros = 0

    while (n):
        if (n & 1 == 1):
            ones += 1
        else:
            zeros += 1

        n = n >> 1

    print("\n\nOnes = ", ones, "\nZeros = ", zeros)


number = int(input("Enter Your Number: "))
numberOfBits(number)
