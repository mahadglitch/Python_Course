# write in file using with()function
with open("Codingal.txt","w") as file:
    file.write("A new text in the write mode")
file.close()

# split file into words
with open("Codingal.txt","r") as file:
    data = file.readlines()
    print("Words in this file are....")
    for line in data:
        word = line.split() # split function used to split sentences into words
        print (word)
file.close        