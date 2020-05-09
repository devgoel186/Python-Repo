import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input("Enter location: ")
fhand=urllib.request.urlopen(url).read()
print("Retrieving", url)
inp=json.loads(fhand)
c=0
sum=0
for item in inp["comments"]:
    c+=1;
    sum+=int(item["count"])
print("Count:", c, "\nSum:", sum)
