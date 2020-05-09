import urllib.request, urllib.parse, urllib.error
#Importing XML tree, abbr as ET
import xml.etree.ElementTree as ET
#Importing SSL for certificate errors
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
xml = urllib.request.urlopen(url, context=ctx).read()

tree= ET.fromstring(xml)
comment=tree.findall('.//count')
sum=0
c=0
for tag in comment:
    sum+=int(tag.text)
    c+=1
print("Count ",c,"\nSum ",sum)
