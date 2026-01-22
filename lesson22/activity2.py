# Program to check if the Nth bit is set or not

def setOrNot(number, n):
    if number & (1 << (n-1)):
        print("\nSET")
    else:
        print("\nNOT SET")\



number = int(input("Enter Your Number: "))
n = int(input("Enter the position of bit to check: "))
setOrNot(number, n)
