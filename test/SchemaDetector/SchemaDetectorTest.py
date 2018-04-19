'''
Created on 19 apr 2018

@author: davideorlando
'''
import unittest
from SchemaDetector.SchemaDetector import SchemaDetector


PATH_KEYWORDS = "../../KeywordsFinder/resources/specifiche.txt"

class SchemaDetectorTest(unittest.TestCase):

    schemaDetector = SchemaDetector()


#     def testSetKeyword(self):
#         with open(PATH_KEYWORDS,"r",encoding="utf8") as fileSpecifiche: 
#             specifiche = fileSpecifiche.read().splitlines()
#         self.schemaDetector.setInformationKeyword(PATH_KEYWORDS)
#         self.assertEqual(set(specifiche),self.schemaDetector.keywords)
#         

#     def testDetectTable_withTable(self):
#         self.assertTrue(self.schemaDetector.detectTable("../testResource/pageWithTable.html"))
#         
#     def testDetectTable_withoutTable(self):
#         self.assertFalse(self.schemaDetector.detectTable("../testResource/pageWithoutTable.html"))

#     def testDetectList_withList(self):
#         self.assertTrue(self.schemaDetector.detectList("../testResource/pageWithList.html"))
#         
#     def testDetectTable_withoutList(self):
#         self.assertFalse(self.schemaDetector.detectList("../testResource/pageWithoutList.html"))

#     def testGetScoreTable_ScoreOne(self):
#             tables = self.schemaDetector.getTablesFromPage("../testResource/pageWithTable.html")
#             self.schemaDetector.setInformationKeyword(PATH_KEYWORDS)
#             self.assertEqual(self.schemaDetector.getScoreTable(tables[4]),15)
#     
    def testGetBestTableScore(self):
        tables = self.schemaDetector.getTablesFromPage("../testResource/pageWithTable.html")
        self.schemaDetector.setInformationKeyword(PATH_KEYWORDS)
        self.assertEqual(self.schemaDetector.getBestTableScore(tables), 15)  

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSetKeyword']
    unittest.main()