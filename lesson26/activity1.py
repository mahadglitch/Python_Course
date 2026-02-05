# Flipping Bits
def f1(n1, n2):
    flips = 0
    while n1 > 0 and n2 > 0:
        t1 = n1 & 1
        t2 = n2 & 1
        if t1 != t2:
            flips += 1
        n1 >>= 1
        n2 >>= 1
    return flips


x = int(input("Enter number 1 : "))
y = int(input("Enter number 2 : "))
print("Number of flips needed : ", f1(x, y))
