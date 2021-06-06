import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore ssl certificates

test_context = ssl.create_default_context()
test_context.check_hostname=False
test_context.verify_mode = ssl.CERT_NONE

url = input('Enter url:')
html = urllib.request.urlopen(url, context=test_context).read()
clean_html = BeautifulSoup(html, 'html.parser')

#retrieve all anchor tags
tags = clean_html('a')
for each_tag in tags:
    print(each_tag.get('href', None))
