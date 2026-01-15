def siev(n):
    prime = [True for i in range(n + 1)]
    p = 2

    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    print("The prime numbers are: ", end="")

    for p in range(2, n + 1):
        if prime[p]:
            print(p, end=" ")


n = int(input("Enter the limit to find all prime numbers up to that limit: "))
siev(n)

# This code finds and prints all prime numbers up to a given limit using the Sieve of Eratosthenes algorithm.
