# Learning to calculate factors of any number in python.
def factors(number):
    print("The factors are ")
    for i in range(1 , number+1):
        if number%i==0:
            print(i)
number = int(input("Enter Your Number"))
factors(number)