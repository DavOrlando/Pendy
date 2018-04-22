
'''
Created on 19 apr 2018
@author: MarcoZebi
'''


import os
from bs4 import BeautifulSoup as bs
import json



class SchemaDetector(object):
    '''

    '''


def estrKeys(pathHtml, Set, attributoClasse):

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
                     Set.add(value)
                     break
    html.close()


def writeSpec(pathFile, Set):

    specifiche = open(pathFile, "w", encoding='utf-8')
    for s in Set:
        if(s != None):
            specifiche.write(s + "\n")
    specifiche.close()


def findHtmlFile(path):
    lista = (os.listdir(path))
    s = set()

    for e in lista:
        if e.find(".html") != -1:
            s.add(e)
    return s


def getdomini2classCss(path):
    pathJson = path + "config.json"
    jsonData = open(pathJson, "r")
    domini2classeCss = json.loads(jsonData.read())
    jsonData.close()
    return domini2classeCss


if __name__ == "__main__":
    path = "./KeywordsFinder/resources/"

    domini2classCss = getdomini2classCss(path)
    specSet = set()

    for dominio in domini2classCss.keys():
        classCss = str(domini2classCss.get(dominio))
        pathDominioHtml = path + "/" + dominio;
        SetFileHtml = findHtmlFile(pathDominioHtml)
        for html in SetFileHtml:
            estrKeys(pathDominioHtml + "/" + html, specSet, classCss)

    writeSpec(path + "specifiche.txt", specSet)
