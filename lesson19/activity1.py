n = int(input("Enter Your Number :"))
original = n
reverse = 0
while n>0:
    digit = n%10
    reverse = reverse*10+digit
    n = n//10
if (original==reverse):
    print("Palindrome number")
else:
    print("Not a palindrome number")