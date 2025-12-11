outputFile = open("no_repeat.txt","w")
inputFile = open ("sample_doc.txt","r")
lines_seen_so_far = set()
print("Eliminating duplicate words....")
for line in inputFile:
    if line not in lines_seen_so_far:
        outputFile.write(line)
        lines_seen_so_far.add(line)


inputFile.close()
outputFile.close()