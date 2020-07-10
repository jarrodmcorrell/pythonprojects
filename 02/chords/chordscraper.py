import requests
from bs4 import BeautifulSoup
import urllib.request

fcnames = []
links = []

data = requests.get('https://www.chordie.com/chords.php')

soup = BeautifulSoup(data.text, 'html.parser')

opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

for a in soup.find_all('a'):
    for img in a.find_all('img'):
        chordname = img['alt'].split("=", 1)[0]
        fcnames.append(chordname)

        link = img['src']
        links.append(link)

for i in range(1, len(links)): 
    print("downloading: " + fcnames[i] + " " + links[i])          

    urllib.request.urlretrieve(links[i], "02/chords/" + fcnames[i].replace('/', '_') + ".png")
    




