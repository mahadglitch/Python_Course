file = open("codingal.txt","r")
print(file.read())
file.close()


file = open("codingal.txt","r")
print("\nRead first 10 chareacters \n")
print(file.read(10))
file.close


file = open("codingal.txt","a")
file.write("\nAppended Text")
file.close