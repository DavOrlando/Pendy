
import scrapy
import os
import regex as re
from bs4 import BeautifulSoup as bs

path="./KeywordsFinder/resources/"
filehtml="2.html"

html= open(path+filehtml,"r+", encoding = 'utf-8')
specSet= set()

soup = bs(html, 'html.parser')
table = soup.find('table', {'class': 'table table-striped'})
rows = table.findChildren(['th', 'tr'])
for row in rows:
     cells = row.findChildren('td')

     for cell in cells:
         value = cell.string
         specSet.add(value)
         break

specifiche=open(path+"specifiche.txt","a", encoding = 'utf-8')
for s in spec:
     specifiche.write(s+"\n")


specifiche.close()
html.close()
