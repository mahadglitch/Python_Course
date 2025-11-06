height = float(input("Enter Your Height"))
weight = float(input("Enter Your Weight"))
BMI = weight/(height/100)**2
if BMI<=18.4:
    print("You Are UnderWeight")
elif BMI<=24.9:
    print("You Are Healthy")
elif BMI<=29.9:
    print("You Are OverWeight")
elif BMI<=34.9:
    print("You Are Severely OverWeight") 
elif BMI<=39.9:
    print("You Are Obese")               
else :
    print("You Are Severely Obese")