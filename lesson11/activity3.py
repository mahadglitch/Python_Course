file = open("codingal.txt","r")
counter = 0
content = file.read()
c = content.split("\n")
for i in c :
    if i:
        counter = counter + 1
print("Number of lines in the file ",counter)        