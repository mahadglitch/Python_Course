small = int(input("Enter your smallest number: "))
high = int(input("Enter your largest number:"))

while(small):
    small_new = small
    small = high%small
    high = small_new
print("The HCF is : ",high)    