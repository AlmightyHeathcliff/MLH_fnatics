 

import requests
from bs4 import BeautifulSoup


x = input()
temp = requests.get('https://www.meetup.com/find/events/?allMeetups=false&keywords='+x+'&radius=25&userFreeform=Delhi%2C+India&mcId=c1018091&mcName=Delhi%2C+IN')
 
soup = BeautifulSoup(temp.text,'lxml')
text_file = open("Outzero.txt", "w")

ls = []
ys = []
z123 = []
#link = soup.find_all('div', class_ = 'd-inline-block event-card-wrp valign-top ga-card-track browse-card')
geez =  soup.findAll('a', {'class': 'resetLink big event wrapNice omnCamp omngj_sj7es omnrv_fe1 chunk'})
'''' loop to iterate all th emeetup groups doing stuff '''''
for d in geez:      
        y = d['href']
        ls.append(y)
                  

''' loop to remove duplicate entries '''
for  i in ls:
    if i not in ys:
         ys.append(i)
   
date1 = []
for links in ys:
    
    temp1 = requests.get(links)
    coup = BeautifulSoup(temp1.text,'lxml')
    geezlo =  coup.findAll('a', {'class': 'eventCard--link'})
    y1 = coup.findAll('span', {'class': 'dateDisplay-day'})
    z1 = coup.findAll('span', {'class': 'dateDisplay-month text--tiny'})
    try:
            z123.append(geezlo[0].text+" "+y1[0].text+" "+z1[0].text+" "+"https://www.meetup.com"+geezlo[0]['href']+" "+"\n")
    except:
            pass
    
    
        
final = ""
for i in z123:
   final.append(z123)