# The program will prompt for a URL, read the JSON data from that URL using urllib
# and then parse and extract the comment counts from the JSON data,
# compute the sum of the numbers in the file and enter the sum below:

import urllib.request, urllib.parse, urllib.error
import json
import ssl

url = ('http://py4e-data.dr-chuck.net/comments_42.json')

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
info = json.loads(data)

sum = 0
for item in info["comments"]:
    sum += int(item["count"])
    
print(sum)
