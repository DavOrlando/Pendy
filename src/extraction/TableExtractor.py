'''
Created on 20 apr 2018

@author: ciroliviero
'''

import detection.SchemaDetector as sd
import json

class TableExtractor(object):
    '''
    An extractor of informations that works on HTML tables.
    extraction produces a dictionary of pairs <key,value>
    from the 'best' table in the page (the table with the best
    score according to its density of keywords)
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.detector = sd.SchemaDetector()
        self.detector.setInformationKeyword("../../resources/specifiche.txt")
    
    def extractSpecificationsFromPage(self,htmlFile):
        try:
            specificationDictionary = {}
            tableWithSpecifications = self.detector.getBestTable(
                self.detector.getTablesFromPage(htmlFile))
            for index,row in tableWithSpecifications.iterrows():
                chiave = str(row[0]).strip().lower()
                if(row[1]==':'):
                    valore= str(row[2]).strip().lower()
                else: valore = str(row[1]).strip().lower()
                specificationDictionary[chiave] =valore
            #print(specificationDictionary)
            return specificationDictionary
        except:
            return {}
    
    def saveSpecificationDictionaryAsJson(self,dictionary,name,domainPath):
        '''TODO Da rifattorizzare: 
        questo metodo deve essere comune a tutti gli estrattori!'''
        with open(domainPath+'/'+name+'.json', 'w',encoding="utf8") as outputJson:
            json.dump(dictionary,outputJson,indent=4,ensure_ascii=False)