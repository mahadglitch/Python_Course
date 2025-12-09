file_read = open("codingal.txt","r")
print("File In Read Mode -")
print(file_read.read())



file_write = open("codingal.txt",'w')
file_write.write("File in write mode....")
file_write.write("\nThis is a write mode text")
file_write.close()



file_append = open("codingal.txt","a")
file_append.write("\nFile in append mode....")
file_append.write("\nThis is an appended text")
file_append.close()