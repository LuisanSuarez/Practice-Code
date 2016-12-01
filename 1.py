import requests

address = 'nostarch.com/automatestuff/'
res = requests.get('https://'+address)

wFile = open('parsing.txt', 'w')

for i in res.iter_content(10000):
    wFile.write(i)
    
wFile.close()
    