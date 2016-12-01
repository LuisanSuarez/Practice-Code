#!/bin/env python
#!/bin/env python2.7

import webbrowser
import requests

'automatetheboringstuff.com/files/rj.txt'
address = 'weather.gov'

res = requests.get('https://'+address)
try:
    res.raise_for_status()
except Exception as e:
    print ('There was a problem: %s' %(e))
print type(res)

playFile = open('Test2.txt', 'w')
for i in res.iter_content(10000):
    playFile.write(i)
    
playFile.close()

#check if the request for the webpage succeeded
  #check status_code attribute of response object
print 'Succeeded?: ', res.status_code == requests.codes.ok



#webbrowser.open('http://inventwithpython.com/')



address = '870 Valencia St, San Francisco, CA 94110'

#webbrowser.open('https://www.google.com/maps/place/' + address)



'''if len(sys.argv)>1:
    #Get address from command line
    address = ' '.join(sys.argv[1:])
    
else:
    address = pyperclip.paste()'''