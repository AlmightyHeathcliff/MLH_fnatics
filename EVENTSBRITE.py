# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 17:52:27 2018

@author: ashie
"""

 

import requests
from bs4 import BeautifulSoup


x = input()
temp = requests.get('https://www.eventbrite.com/d/india--delhi/'+x+'/')
soup = BeautifulSoup(temp.text,'lxml')

ls = []
ys = []
z123 = []

try:
#link = soup.find_all('div', class_ = 'd-inline-block event-card-wrp valign-top ga-card-track browse-card')
   geez =  soup.findAll('div', {'class': 'eds-is-hidden-accessible'})
#leez =  soup.findAll('div', {'class': 'eds-text-bs--fixed eds-text-color--grey-600 eds-l-mar-top-1'})
   keez =  soup.findAll('div', {'class': 'eds-media-card-content__sub-content'})
   med = int(0)

   for l in keez:
      y = soup.findAll('div', {'class': 'eds-text-bs--fixed eds-text-color--grey-600 eds-l-mar-top-1'})
      z = soup.findAll('div', {'class': 'card-text--truncated__one'})
      ls.append(str(med)+"             ||            "+str(geez[med].text)+"             ||             "+str(y[med].text)+"                ||                "+str(z[med].text)+ "\n")
      med = med+1
except:
   pass


final = ""
for i in ls:
   final = final + i
   final = final + "\n"
   
   
text_file = open("eventsBRITE.txt", "a")
text_file.write(final)
text_file.close()    