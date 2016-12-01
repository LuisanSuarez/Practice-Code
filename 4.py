import bs4
soup = bs4.BeautifulSoup(open('example.html'))
spanElem = soup.select('span')[0]
print'1: ', str(spanElem)
print spanElem.get('id')

print spanElem.get('some:nonexisten') == None

print spanElem.attrs
