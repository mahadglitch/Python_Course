# check if a number is power of 2
def f1(n):
    if n == 0:
        return 0
    if (n & (n-1) == 0):
        return 1
    return 0


n = int(input("Enter a number: "))
if f1(n):
    print(n, "is a power of 2")
else:
    print(n, "is not a power of 2")

'''
n=8
8=1000
&
7=0111
  0000
  
'''
n = int(input("Enter a number: "))
m = n
if n == 0:
    print(m, "is not a power of 2")
else:
    while n % 2 == 0:
        n = n//2
    if n == 1:
        print(m, "is a power of 2")
    else:
        print(m, "is not a power of 2")
