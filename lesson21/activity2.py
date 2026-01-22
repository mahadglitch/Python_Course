def isevenodd(n):
    if (n ^ 1 == n+1):
        return True
    else:
        return False


n = int(input("Enter Your Number: "))
if isevenodd(n):
    print("Even Number.")
else:
    print("Odd Number")
