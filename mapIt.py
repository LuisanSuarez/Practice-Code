import webbrowser, sys
import requests

link = 'https://automatetheboringstuff.com/files/rj.txt'
link2 = 'https://automatetheboringstuff.com/unexistent_page'
 
res = requests.get(link)
try:
    res.raise_for_status()
except Exception as exc:
    print ('There was a problem: %s' % (exc))

playFile = open('RomeoAndJulietSwift.txt', 'wb')

for chunk in res.iter_content(10000):
    playFile.write(chunk)
    
    
playFile.close()