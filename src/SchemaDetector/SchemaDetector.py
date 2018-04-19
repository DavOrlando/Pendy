'''
Created on 19 apr 2018

@author: davideorlando
'''

import pandas as pd

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
        except:
            print("A problem occurred during creation of keyword set")
    
    
    def detectTable(self, htmlFile):
        try:
            tables = pd.read_html(htmlFile)
            if(len(tables)>0):
                print(htmlFile+" contains table")
                return True;
            return False;
        except:
            print("A problem occurred during detection of tables or no table inside "+htmlFile)
            return False;

    def detectList(self, htmlFile):
            try:
                lists = pd.read_html(htmlFile)
                
            except:
                print("A problem occurred during detection of tables or no table inside page")
                return False;
