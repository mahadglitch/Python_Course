def factorial(number):
    if number==1:
        return number
    else:
        return number*factorial(number-1)
number = int(input("Enter Your Number To Calculate Factorial"))   
if number<0:
    print("Factorial Does Not Exist For Negetive Numbers")
elif number==0:
    print("The Factorial Of 0 Is 1")
else:
    print("The Factorial Is " , factorial(number))        