'''
Created on 20 apr 2018

@author: ciroliviero
'''
import unittest
from extraction.ListExtractor import ListExtractor

class TableEstractorTest(unittest.TestCase):
    extractor = ListExtractor()

    def testExtractSpecificationsFromPage_minimalListPage(self):
        dictionary = self.extractor.extractSpecificationsFromPage("../testResource/minimalListPage.html")
        self.assertEqual(dictionary, {'Resolution': '1920 x 1080', 'Response Time': '5ms', 'Interfaces': 'VGA'})
     
    def testExtractSpecificationsFromPage_listPageWithLiWithoutKeywordsMatched(self):
        dictionary = self.extractor.extractSpecificationsFromPage("../testResource/listPageWithLiWithoutKeywordsMatched.html")
        self.assertEqual(dictionary, {'Interfaces': 'HDMI'})
    
    def testExtractSpecificationsFromPage_listPageWithLiWithUnknownValue(self):
        dictionary = self.extractor.extractSpecificationsFromPage("../testResource/listPageWithLiWithUnknownValue.html")
        self.assertEqual(dictionary, {'Interfaces': 'HDMI'})
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()