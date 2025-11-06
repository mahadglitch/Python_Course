def add( x , y ) :
    return x+y
def subtract( x , y ) :
    return x-y
def multiply( x , y ) :
    return x*y
def divide( x , y ) :
    return x/y
x = int(input("Enter Your First Number "))
y = int(input("Enter Your Second Number"))
print("Addition: " , add( x , y ))
print("Subtraction: " , subtract( x , y ))
print("Multiplication: " , multiply( x , y ))
print("Division: " , divide( x , y ))