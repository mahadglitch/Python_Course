# Seeing if a number is prime or not.
from math import sqrt
n = int(input("Enter Your Number : "))
if n > 1:
    is_prime = True
    for i in range(2, int(sqrt(n))+1):
        if (n % i) == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime Number.")
    else:
        print("Not a prime number.")
else:
    print("Not a prime number.")
