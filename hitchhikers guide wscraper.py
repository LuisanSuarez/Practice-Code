from lxml import html
import requests

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)

#buyers = tree.xpath('//div[@title = "buyer-name"]/text()')

#prices = tree.xpath('//span[@class="item-price"]/text()')

example = tree.xpath('//div[@class="documentwrapper"]/child')

'''print 'Buyers are: ', buyers
print 'Prices seem to be: ', prices'''

print 'Example: ', example

