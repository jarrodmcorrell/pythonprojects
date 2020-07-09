import requests
import re
import sys
import os

url = input("Enter url:")
print("searching url: " + url)

data = requests.get(url)

emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)

print(emails)
