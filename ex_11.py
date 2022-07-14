# In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.
# Using regular expressions

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "actual.txt"

import re

fhand = open(fname)
count = 0
tot = 0

numlist = list()

for line in fhand:
    line = line.rstrip()
    x = re.findall('[0-9]+',line)
    for i in x:
        tot = tot + int(i)
        count = count + 1

print("Count :",count)
print("Total :",tot)
