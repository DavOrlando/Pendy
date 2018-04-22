'''
Created on 20 apr 2018

@author: ciroliviero
'''

import SchemaDetector.SchemaDetector as sd
import json
from builtins import str

class ListExtractor(object):
    '''
    An extractor of informations that works on HTML lists.
    ListExtractor produces a dictionary of pairs <key,value>
    from the 'best' list in the page (the list with the best
    score according to its density of keywords)
    '''


    def __init__(self,):
        '''
        Constructor
        '''
        'DA RIFATTORIZZARE'
        self.specification2ExpectedValues = self.loadSpecificationExpectedValuesDictionary("../../test/testResource/testExpectedValues.json")
        self.detector = sd.SchemaDetector()
        'DA RIFATTORIZZARE'
        self.detector.setInformationKeyword("../../resources/specifiche.txt")
    
    def loadSpecificationExpectedValuesDictionary(self,path):
        return json.load(open(path))
    
    def extractSpecificationsFromPage(self,htmlFile):
        specificationDictionary = {}
        listWithSpecifications = self.detector.getBestList(
            self.detector.getListsFromPage(htmlFile))
        if(listWithSpecifications==None):
            return {}
        for li in listWithSpecifications.findAll("li"):
            for key in self.specification2ExpectedValues:
                if(str(li).find(key)>-1):
                    for value in self.specification2ExpectedValues[key]:
                        if(str(li).find(value)>-1):
                            specificationDictionary[key] = value
                            break
        return specificationDictionary
    
    def saveSpecificationDictionaryAsJson(self,dictionary,name,domainPath):
        '''TODO Da rifattorizzare: 
        questo metodo deve essere comune a tutti gli estrattori!'''
        with open(domainPath+'/'+name+'.json', 'w') as outputJson:
            json.dump(dictionary,outputJson,indent=4,ensure_ascii=False)
        