# This file will input numbers until done is inputed
# It will return the sum, and count and the average

num = 0
total = 0

while True:
    sval = input("Enter a number: ")
    if sval == 'done':
        break

    try:
        fval = float(sval)
    except:
        print('Invalid Input')
        continue

    num = num + 1
    total = total + fval

print("total   :",total)
print("count   :", num)
print("average :", total/num)
