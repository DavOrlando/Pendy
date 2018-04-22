'''
Created on 19 apr 2018

@author: davideorlando
'''

import pandas as pd
from bs4 import BeautifulSoup
from _ast import keyword
from pip._vendor.distlib.locators import Page
from pandas.plotting._tools import table

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
    
    def setInformationKeyword(self,keywordsPath):
        try:
            with open(keywordsPath,"r",encoding="utf8") as keywordsFile: 
                self.keywords = set([x.strip().lower() for x in keywordsFile.read().splitlines()])
            print("Set of Keywords created")
        except Exception as e:
            print("A problem occurred during creation of keyword set")
            print(e)
    
    
    def detectTable(self, htmlFile):
        try:
            if(len(self.getTablesFromPage(htmlFile))>0):
                print(htmlFile+" contains table")
                return True;
            return False;
        except Exception as e:
            print("A problem occurred during detection of tables or no table inside "+htmlFile)
            print(e)
            return False;

    def detectList(self, htmlFile):
        try:
            with open(htmlFile,"r",encoding="utf8") as page: 
                soup = BeautifulSoup(page.read(), 'lxml')
            if(soup.find("ol")!=None or soup.find("ul") !=None):
                print(htmlFile+" contains lists")
                return True
            else:
                print("No lists inside "+htmlFile)
                return False
        except Exception as e:
            print("A problem occurred during detection of lists inside "+htmlFile)
            print(e)
            return False
        
    def getTablesFromPage(self,htmlFile):
        try:
            return pd.read_html(htmlFile)
        except:
            return None
  
    
    def getScoreTable(self, table):
        titles = [str(x).lstrip().lower() for x in list(table[0])]
        return len(list(set(titles).intersection(self.keywords)))
    
    def getBestTableScore(self, tables):
        return self.getScoreTable(self.getBestTable(tables))
    
    def getBestTable(self,tables):
        indexBest = -1
        best = 0
        for index in range(0,len(tables)):
            temp = self.getScoreTable(tables[index])
            if(temp > best):
                indexBest = index
                best = temp
        return tables[indexBest]
             
    def getListsFromPage(self,htmlFile):
        with open(htmlFile,"r",encoding="utf8") as page: 
                soup = BeautifulSoup(page.read(), 'lxml')
        lista = soup.findAll("ol")
        lista+=soup.findAll("ul")
        print(lista)
        return lista
          
             

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

    def getScoreList(self, lista):
        keywordsFromList = self.getKeywordsFromList(lista)
        return len(list(set(keywordsFromList).intersection(self.keywords)))
    
    def getBestListsScore(self, lists):
        return self.getScoreList(self.getBestList(lists))

    def calculateTableScore(self,page,tables):
        if(self.detectTable(page)):
            return self.getBestTableScore(tables)
        else: return 0    

    def calculateListsScore(self,page,lists):
        if(self.detectList(page)):
            return self.getBestListsScore(lists)
        else: return 0    

    def getBestList(self,liste):
        bestList=[]
        best = 0
        for lista in liste:
            temp = self.getScoreList(lista)
            if(temp >= best):
                if(temp == best):
                    bestList.append(lista)
                else:
                    bestList=lista
                    best = temp
        print("DIOOOO BOOO" + str(bestList))
        return bestList


    def detect(self,pages):        
        listCount=0
        tableCount=0
        for page in pages:
            listScore = self.calculateListsScore(page, self.getListsFromPage(page))
            tableScore = self.calculateTableScore(page, self.getTablesFromPage(page))
            if(listScore>tableScore):
                listCount+=1
            if(tableScore>listScore): 
                tableCount+=1
        print(tableCount)
        print(listCount)
        if (tableCount>listCount):
            return "table"
        if (listCount>tableCount):
            return "list"
        if(listCount==0 and tableCount==0):
            return "text"
        if(listCount==tableCount):
            return "table"