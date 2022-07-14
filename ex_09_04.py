# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

counts = dict()
add = []

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fhand = open(fname)
for line in fhand:
    if not line.startswith("From") or line.startswith("From:"):
        continue
    linelist = line.split()
    word = linelist[1]
    add.append(word)
    counts[word] = counts.get(word,0) + 1

# this part will count through the histogram
bigword = None
bigcount = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
        
print(bigword,bigcount)
