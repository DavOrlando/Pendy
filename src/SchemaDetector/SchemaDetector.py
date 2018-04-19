'''
Created on 19 apr 2018

@author: davideorlando
'''

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
        fileSpecifiche = open(keywordsPath,"r")       
        specifiche = fileSpecifiche.read().splitlines()
        fileSpecifiche.close()
        self.keywords = set(specifiche)

        
        