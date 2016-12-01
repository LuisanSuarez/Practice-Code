import requests
from bs4 import BeautifulSoup
import pandas

url = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

res = requests.get(url)

soup = BeautifulSoup(res.content)

all_tables = soup.find_all('table')

right_table = soup.find_all('table',\
{"class" : "wikitable sortable plainrowheaders"})

#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]


for row in right_table[0].find_all("tr"):
    cells = row.find_all("td")
    states = row.find_all("th")
    if len(cells) == 6:
        A.append(cells[0].text)
        B.append(states[0].text)
        C.append(cells[1].text)
        D.append(cells[2].text)
        E.append(cells[3].text)
        F.append(cells[4].text)
        G.append(cells[5].text)
        
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G
df
    