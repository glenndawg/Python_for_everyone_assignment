# The program will prompt for a URL, read the XML data from that URL using urllib
# and then parse and extract the comment counts from the XML data,
# compute the sum of the numbers in the file.

from urllib import request
import xml.etree.ElementTree as ET

url = ('http://py4e-data.dr-chuck.net/comments_42.xml')
xml = request.urlopen(url)
data = xml.read()

tree = ET.fromstring(data)
list = tree.findall('comments/comment')
print('Comment count:', len(list))

sum = 0
for items in list:
    sum += float(items.find('count').text)

print('Sum :', sum)
