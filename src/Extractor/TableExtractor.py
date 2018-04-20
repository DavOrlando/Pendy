'''
Created on 20 apr 2018

@author: ciroliviero
'''

import SchemaDetector.SchemaDetector as sd
import json

class TableExtractor(object):
    '''
    An extractor of informations that works on HTML tables.
    Extractor produces a dictionary of pairs <key,value>
    from the 'best' table in the page (the table with the best
    score according to its density of keywords)
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.detector = sd.SchemaDetector()
        'DA RIFATTORIZZARE'
        self.detector.setInformationKeyword("../KeywordsFinder/resources/specifiche.txt")
    
    def extractSpecificationsFromPage(self,htmlFile):
        specificationDictionary = {}
        tableWithSpecifications = self.detector.getBestTable(
            self.detector.getTablesFromPage(htmlFile))
        for index,row in tableWithSpecifications.iterrows():
            specificationDictionary[row[0]] = row[1]
        #print(specificationDictionary)
        return specificationDictionary
    
    def saveSpecificationDictionaryAsJson(self,dictionary,name,domainPath):
        '''TODO Da rifattorizzare: 
        questo metodo deve essere comune a tutti gli estrattori!'''
        with open(domainPath+'/'+name+'.json', 'w') as outputJson:
            json.dump(dictionary,outputJson,indent=4,ensure_ascii=False)