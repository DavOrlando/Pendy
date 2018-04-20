'''
Created on 20 apr 2018

@author: ciroliviero
'''
import unittest
from Utils.ExpectedValuesFinder import ExpectedValuesFinder
import json
import os

class ExpectedValuesFinderTest(unittest.TestCase):
    outputPath = "../testResource/ExpectedValues.json"
    evf = ExpectedValuesFinder(outputPath)

    def testUpdateExpectedValue_emptyDictionary(self):
        self.evf.updateExpectedValues({})
        with open(self.outputPath,"r") as testValuesFile:
            testValues = json.load(testValuesFile)
            self.assertEqual(testValues, {})
            
    def testUpdateExpectedValue_minimalDictionary(self):
        self.evf.updateExpectedValues({'A': 'x1', 'B': 'y1'})
        with open(self.outputPath,"r") as testValuesFile:
            testValues = json.load(testValuesFile)
            self.assertEqual(testValues['A'], ['x1'])
            self.assertEqual(testValues['B'], ['y1'])
            
    def testUpdateExpectedValue_newValueForExistingKey(self):
        '''The assumption for this test is that before the test:  
        testValuesFile is in this condition:
        {'A': ['x1'], 'B': ['y1']}'''
        self.evf.updateExpectedValues({'A': 'x2'})
        with open(self.outputPath,"r") as testValuesFile:
            testValues = json.load(testValuesFile)
            self.assertEqual(testValues['A'], ['x1','x2'])

    @classmethod
    def tearDownClass(cls):
        os.remove("../testResource/ExpectedValues.json")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()