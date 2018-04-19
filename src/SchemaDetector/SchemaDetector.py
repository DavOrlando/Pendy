'''
Created on 19 apr 2018

@author: davideorlando
'''

import pandas as pd
from bs4 import BeautifulSoup

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
            with open(keywordsPath) as keywordsFile: 
                self.keywords = set(keywordsFile.read().splitlines())
            print("Set of Keywords created")
        except Exception as e:
            print("A problem occurred during creation of keyword set")
            print(e)
    
    
    def detectTable(self, htmlFile):
        try:
            tables = pd.read_html(htmlFile)
            if(len(tables)>0):
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
