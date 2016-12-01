import bs4
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select('#author')
#print type(elems)
#print len(elems)
#print type(elems[0])
for i in range((len(elems))): print elems[i].getText() 
for i in range((len(elems))): print str(elems[i])
for i in range((len(elems))): print elems[i].attrs