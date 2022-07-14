# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

counts = dict()
add = []

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

# this parts splits out the text to make a list of hours
fhand = open(fname)
for line in fhand:
    if not line.startswith("From") or line.startswith("From:"):
        continue
    linelist = line.split()
    time = linelist[5]
    time = time.split(':')
    hour = time[0]
    add.append(hour)
    counts[hour] = counts.get(hour,0) + 1

# this part prints in key, value list
temp = sorted([(k,v) for k,v in counts.items()])
for k,v in temp:
    print(k,v)
