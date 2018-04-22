'''
Created on 19 apr 2018

@author: davideorlando
'''

import pandas as pd
from bs4 import BeautifulSoup
from builtins import str
from _ast import Str

class SchemaDetector(object):
    '''
    A detector of how informations are organized 
    in the page of a website. 
    For example if a domain, as www.xyz.com, 
    organizes informations in tables then 
    the detector labels the domain as domain with tables.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.keywords = set()
    
    def setInformationKeyword(self, keywordsPath):
        try:
            with open(keywordsPath, "r", encoding="utf8") as keywordsFile: 
                self.keywords = set([x.strip().lower() for x in keywordsFile.read().splitlines()])
            print("Set of Keywords created")
        except Exception as e:
            print("A problem occurred during creation of keyword set")
            print(e)
    
    def detectTable(self, htmlFile):
        try:
            if(len(self.getTablesFromPage(htmlFile)) > 0):
                print(htmlFile + " contains table")
                return True;
            return False;
        except Exception as e:
            print("A problem occurred during detection of tables or no table inside " + htmlFile)
            print(e)
            return False;

    def detectList(self, htmlFile):
        try:
            with open(htmlFile, "r", encoding="utf8") as page: 
                soup = BeautifulSoup(page.read(), 'lxml')
            if(soup.find("ol") != None or soup.find("ul") != None):
                print(htmlFile + " contains lists")
                return True
            else:
                print("No lists inside " + htmlFile)
                return False
        except Exception as e:
            print("A problem occurred during detection of lists inside " + htmlFile)
            print(e)
            return False
        
    def getTablesFromPage(self, htmlFile):
        try:
            return pd.read_html(htmlFile)
        except Exception as e:
            print(e)
            return None
        
    def getListsFromPage(self, htmlFile):
        with open(htmlFile, "r", encoding="utf8") as page: 
                soup = BeautifulSoup(page.read(), 'lxml')
        lista = soup.findAll("ol")
        lista += soup.findAll("ul")
        if(lista):
            return lista
        return None
               
    def calculateTableScore(self, tables):
        if(tables != None):
            return self.getScoreTable(self.getBestTable(tables))
        return 0    
    
    def getScoreTable(self, table):
        try:
            titles = [str(x).lstrip().lower() for x in list(table[0])]
            return len(list(set(titles).intersection(self.keywords)))
        except:
            print("Non è possibile trovare un punteggio per le tabelle")
            return 0
        
    def getBestTable(self, tables):
        try:
            indexBest = -1
            best = 0
            for index in range(0, len(tables)):
                temp = self.getScoreTable(tables[index])
                if(temp > best):
                    indexBest = index
                    best = temp
            return tables[indexBest]
        except:
            return None
    
    def calculateListsScore(self, lists):
        if(lists != None):
            return self.getScoreList(self.getBestList(lists))
        return 0

    def getBestList(self, liste):
        bestList = None
        best = 0
        for lista in liste:
            temp = self.getScoreList(lista)
            if(temp > best):
                bestList = lista
                best = temp
        return bestList

    def getScoreList(self, lista):
        keywordsFromList = self.getKeywordsFromList(lista)
        return len(list(set(keywordsFromList).intersection(self.keywords)))
    
    def getKeywordsFromList(self, lista):
        try:
            keywordsFromList = []
            for li in lista.findAll("li"):
                if (":" in li.text):
                    keywordsFromList.append(li.text.partition(':')[0].lstrip())
                else:
                    keywordsFromList.append(li.text.partition(' ')[0].lstrip())
            
            keywordsFromList = [x.lower() for x in keywordsFromList]
            return keywordsFromList
        except:
            return []
 
    def detect(self, pages):        
        numberOfPagesWithList = 0
        numberOfPagesWithTables = 0
        for page in pages:
            tableScore = self.calculateTableScore(self.getTablesFromPage(page))
            listScore = self.calculateListsScore(self.getListsFromPage(page))
            if(tableScore >= listScore and tableScore != 0):
                numberOfPagesWithTables += 1
            if(listScore > tableScore):
                numberOfPagesWithList += 1
        if (numberOfPagesWithTables >= numberOfPagesWithList and numberOfPagesWithTables != 0):
            return "table"
        if (numberOfPagesWithList > numberOfPagesWithTables):
            return "list"
        return "text"
        
