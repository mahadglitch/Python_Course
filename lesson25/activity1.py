a = int(input("Enter a : "))
b = int(input("Enter b : "))
print("The numbers before swapping : a=", a, "b=", b)
a, b = b, a
print("The numbers after swapping : a=", a, "b=", b)
# swap without 3rd variable


def swap1(a, b):  # without bit operation
    print("Before Swapping : ", a, b)  # a=30,b=40
    a = a+b  # a=30+40 =70
    b = a-b  # b=70-40=30
    a = a-b  # a=70-30=40
    print("After Swapping : ", a, b)


def swap2(a, b):  # using bit operation
    print("Before Swapping : ", a, b)  # 1100 , 0101
    a = a ^ b  # a=1100 ^ 0101=1001
    b = a ^ b  # b=1001^0101=1100
    a = a ^ b  # a=1001^1100=0101
    print("After Swapping : ", a, b)


def swap3(a, b):  # using bit operation
    print("Before Swapping : ", a, b)
    a = (a & b)+(a | b)
    b = a+(~b)+1
    a = a+(~b)+1
    print("After Swapping : ", a, b)


'''
1100 , 0101
a&b =1100 & 0101= 0100
a|b =1100 | 0101 =1101
a= (a&b)+(a|b)   =10001
b=a+(~b)+1=10001
          +01010
          +00001
        b= 11100
0+0=0, 0+1=1, 1+1=10, 1+1+1=11
a=a+(~b)+1=10001
          +00011
          +00001
           10101

'''
swap1(30, 40)
swap2(30, 40)
swap3(30, 40)
