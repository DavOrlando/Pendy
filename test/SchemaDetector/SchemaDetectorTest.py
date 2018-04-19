'''
Created on 19 apr 2018

@author: davideorlando
'''
import unittest
from SchemaDetector.SchemaDetector import SchemaDetector


PATH_KEYWORDS = "../../KeywordsFinder/resources/specifiche.txt"

class SchemaDetectorTest(unittest.TestCase):

    schemaDetector = SchemaDetector()


    def testSetKeyword(self):
        fileSpecifiche = open(PATH_KEYWORDS,"r")       
        specifiche = fileSpecifiche.read().splitlines()
        fileSpecifiche.close()
        self.schemaDetector.setInformationKeyword(PATH_KEYWORDS)
        self.assertEqual(set(specifiche),self.schemaDetector.keywords)
        

    def testDetectTable_withTable(self):
        self.assertTrue(self.schemaDetector.detectTable(
            "https://www.amazon.it/Sharp-Aquos-Smart-Harman-Kardon/dp/B0799CLDXG/ref=sr_1_1?s=electronics&ie=UTF8&qid=1524134218&sr=1-1"))
        
    def testDetectTable_withoutTable(self):
        self.assertFalse(self.schemaDetector.detectTable("https://ogle.it"))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSetKeyword']
    unittest.main()