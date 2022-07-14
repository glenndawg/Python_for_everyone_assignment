# The program will use urllib to read the HTML from the data files below,
# and parse the data, extracting numbers and
# compute the sum of the numbers in the file.



import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter : ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
spans = [int(tag.contents[0]) for tag in tags]
tot = sum(spans)

print(tot)
