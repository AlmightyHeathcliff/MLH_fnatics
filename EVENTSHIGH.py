
"""
Created on Sat Dec  1 13:10:38 2018

@author: ashie
"""

import requests
from bs4 import BeautifulSoup
import re,csv
import pandas as pd



#tag2    
x = input()
temp = requests.get("https://www.eventshigh.com/search?city=delhi&interest="+x)
# use bs
soup = BeautifulSoup(temp.text,'lxml')
text_file = open("Outzero.txt", "w")

ls = []
#tag1
#link = soup.find_all('div', class_ = 'd-inline-block event-card-wrp valign-top ga-card-track browse-card')
geez =  soup.findAll('div', {'class': 'd-inline-block event-card-wrp valign-top ga-card-track browse-card'})
x = 'https://www.eventshigh.com'
for div in geez:
    y = div.find('a')['href']
    z = x+y
    ls.append(z)
    
    


    
time=1

for i in ls:
   
   temp = requests.get(i)
   soup = BeautifulSoup(temp.text,'lxml')
   text_file = open("Output.txt", "w")
   movie_containers = soup.find_all('div', class_ = 'eh-main-details-desc')
   link = soup.find_all('a', class_ = 'eh-btn eh-book-btn')
   likey = link[0]
   

   
   s = likey['onclick']
   link = re.search(r'\((.*?)\)',s).group(1)

   temp = ""
   company = soup.find('h1')
   company = str(company.text)
   temp = temp + company + ","
   ''' link'''
   for i in range(2):
         p = movie_containers[i].text
         p = p.replace(',', '            ||             ')
         temp = temp+p
         temp = temp+'             ||                 '
         
         

   temp = temp + link[1:-1]
   temp = temp+"\n"+"\n"+"\n"
   text_file = open("eventsHIGH.txt", "a")
   text_file.write(temp)
   text_file.close() 
   
   print(temp)
   
 




         











   





