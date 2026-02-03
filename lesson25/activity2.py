# divide without division operator
def divi(a, b):
    # check if numerator of denominator are +ve or -ve
    sign = (-1 if ((a < 0) ^ (b < 0)) else 1)

    # make both +ve
    a = abs(a)
    b = abs(b)
    q = 0
    temp = 0
    for i in range(31, -1, -1):  # 31 to 0
        if (temp+(b << i) <= a):
            temp += b << i
            q |= 1 << i  # q=q|(1<<i)
    if sign == -1:
        q = -q
    return q


a = int(input("Enter a : "))
b = int(input("Enter b : "))
print(divi(a, b))
'''
n1 = 0111001
n2 = 0011001
n3 = 0111100
shift
0011110
0001111
0000111 -> 1 -> c=1
0000011 -> 1 -> c=2
'''
