
'''
Created on 19 apr 2018
@author: MarcoZebi
'''

from bs4 import BeautifulSoup as bs
import json
from utils.PageBroker import PageBroker


class KeyWordsFinder(object):
    '''

    '''

    
    def estrKeys(self,pathHtml, Set, attributoClasse):
    
        html = open(pathHtml, "r+", encoding='utf-8')
        soup = bs(html, 'html.parser')
        table = soup.find('table', {'class': attributoClasse})
        if (table != None):  # controllo precauzionale
            rows = table.findChildren(['th', 'tr'])
            if rows != None:
                for row in rows:
                    cells = row.findChildren('td')
                    for cell in cells:
                        value = cell.string
                        if(value != None):
                            Set.add(value.lower().rstrip())
                            break
        html.close()
    
    
    def writeSpec(self,pathFile, Set):
    
        specifiche = open(pathFile, "w", encoding='utf-8')
        for s in Set:
            if(s != None):
                specifiche.write(s + "\n")
        specifiche.close()
    
    
    def getdomini2classCss(self,path):
        pathJson = path + "config.json"
        jsonData = open(pathJson, "r")
        domini2classeCss = json.loads(jsonData.read())
        jsonData.close()
        return domini2classeCss
    
    
    def createSpecifications(self):
        path = "../../resources/"
    
        domini2classCss = self.getdomini2classCss(path)
        specSet = set()
    
        for dominio in domini2classCss.keys():
            classCss = str(domini2classCss.get(dominio))
            pathDominioHtml = path + "/" + dominio;
            SetFileHtml = PageBroker().findHtmlFile(pathDominioHtml)
            for html in SetFileHtml:
                self.estrKeys(pathDominioHtml + "/" + html, specSet, classCss)
    
        self.writeSpec(path + "specifiche.txt", specSet)
