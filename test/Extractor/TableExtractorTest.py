'''
Created on 20 apr 2018

@author: ciroliviero
'''
import unittest
from extraction.TableExtractor import TableExtractor

class TableEstractorTest(unittest.TestCase):
    extractor = TableExtractor()

    def testExtractSpecificationsFromPage_minimalTable(self):
        dictionary = self.extractor.extractSpecificationsFromPage("../testResource/minimalTablePage.html")
        self.assertEqual(dictionary, {'Keys': 'Values', 'HDMI': 'Yes', 'VGA': 'No'})
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()