small = int(input("Enter your smallest number: "))
high = int(input("Enter your largest number:"))

if (high > small):
    max = high

while (True):
    if (max % small == 0 and max % high == 0):
        lcm = max
        break
    max = max+1

print("The LCM is :", max)
