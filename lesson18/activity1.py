# Learning Armstrong numbers
number = int(input("Enter Your Number"))
length = len(str(number))
result = 0
temp = number
while temp>0:
    digit = temp%10
    result = result + digit**length
    temp = temp//15310
if number==result:
    print("Armstrong Number.")
else:
    print("Not An Amrstrong Number.")