'''
Created on 20 apr 2018

@author: ciroliviero
'''
import json
import os

class ExpectedValuesFinder(object):
    '''
    classdocs
    '''


    def __init__(self, outputPath):
        '''
        Constructor
        '''
        self.outputPath = outputPath
        if(os.path.exists(self.outputPath)==False):
            with open(self.outputPath,"w",encoding="utf8") as expectedValuesFile: 
                json.dump({},expectedValuesFile)
    
    def updateExpectedValues(self,istanceDictionary):
        with open(self.outputPath,"r+",encoding="utf8") as expectedValuesFile:
            expectedValues = json.load(expectedValuesFile)
            for key in istanceDictionary:
                keyWithoutSpaces = key.rstrip()
                if expectedValues.get(keyWithoutSpaces) == None:
                    expectedValues[keyWithoutSpaces] = []
                expectedValues[keyWithoutSpaces].append(istanceDictionary[key])
            expectedValuesFile.seek(0)
            json.dump(expectedValues,expectedValuesFile,indent=4,ensure_ascii=False)
            expectedValuesFile.truncate()