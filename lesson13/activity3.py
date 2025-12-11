# Program to merge two files into a third file
# Reading data from file 1
with open("Codingal.txt") as fp:
    data1 = fp.read()

# Reading data from file 2
with open("sample_doc.txt") as fp:
    data2 = fp.read()

# Merging 2 files
# To add the data of file 2
# from next line
data1 += "\n"
data2 = data1 + data2
print("Merging two files....")
with open ("MergingFile.txt","w") as fp:
    fp.write(data2)