# 8.4 Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words.
# For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.

length = 0
count = 0

fname = input("Enter file name: ")
fhand = open(fname)

flist = []
for line in fhand:
    linelist = line.split()
    for i in range(len(linelist)):
        if linelist[i] not in flist:
            flist.append(linelist[i])

flist.sort()
print(flist)
