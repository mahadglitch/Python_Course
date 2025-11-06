number = int(input("Enter a number: "))
power = len(str(number))
total = sum(int(digit) ** power for digit in str(number))

if number == total:
    print("It Is An Armstrong number.")
else:
    print("It Is Not an Armstrong number.")

