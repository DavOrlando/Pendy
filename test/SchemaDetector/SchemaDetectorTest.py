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
        with open(PATH_KEYWORDS,"r",encoding="utf8") as fileSpecifiche: 
            specifiche = fileSpecifiche.read().splitlines()
        self.schemaDetector.setInformationKeyword(PATH_KEYWORDS)
        self.assertEqual(set([x.lower().strip() for x in specifiche]),self.schemaDetector.keywords)
         

    def testDetectTable_withTable(self):
        self.assertTrue(self.schemaDetector.detectTable("../testResource/pageWithTable.html"))
         
    def testDetectTable_withoutTable(self):
        self.assertFalse(self.schemaDetector.detectTable("../testResource/pageWithoutTable.html"))

    def testDetectList_withList(self):
        self.assertTrue(self.schemaDetector.detectList("../testResource/pageWithList.html"))
         
    def testDetectTable_withoutList(self):
        self.assertFalse(self.schemaDetector.detectList("../testResource/pageWithoutList.html"))

    def testGetScoreTable(self):
        tables = self.schemaDetector.getTablesFromPage("../testResource/pageWithTable.html")
        self.schemaDetector.setInformationKeyword(PATH_KEYWORDS)
        self.assertEqual(self.schemaDetector.getScoreTable(tables[4]),15)
     
    def testGetBestTableScore(self):
        tables = self.schemaDetector.getTablesFromPage("../testResource/pageWithTable.html")
        self.schemaDetector.setInformationKeyword(PATH_KEYWORDS)
        self.assertEqual(self.schemaDetector.getBestTableScore(tables), 15)  
    
    def testGetBestTable(self):
        tables = self.schemaDetector.getTablesFromPage("../testResource/pageWithTable.html")
        self.schemaDetector.setInformationKeyword(PATH_KEYWORDS)
        self.assertEqual(str(self.schemaDetector.getBestTable(tables)), str(tables[4]))  
 
    def testGetScoreList(self):
        lists = self.schemaDetector.getListsFromPage("../testResource/pageWithList.html")
        self.schemaDetector.setInformationKeyword(PATH_KEYWORDS)
        self.assertEqual(self.schemaDetector.getScoreList(lists[0]),0)
    
    def testGetBestListsScore(self):
        lists = self.schemaDetector.getListsFromPage("../testResource/pageWithList.html")
        self.schemaDetector.setInformationKeyword(PATH_KEYWORDS)
        self.assertEqual(self.schemaDetector.getBestListsScore(lists), 10) 

        
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testSetKeyword']
    unittest.main()
