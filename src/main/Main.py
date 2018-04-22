'''
Created on 22 apr 2018

@author: davideorlando
'''
from keywordsfinding.KeyWordsFinder import KeyWordsFinder
import os
from utils.PageBroker import PageBroker
from detection.SchemaDetector import SchemaDetector
from extraction.TableExtractor import TableExtractor
from utils.ExpectedValuesFinder import ExpectedValuesFinder

PATH_KEYWORDS = "../../resources/specifiche.txt"

if __name__ == '__main__':
    KeyWordsFinder().createSpecifications()
    detector = SchemaDetector()
    tableExtr = TableExtractor()
    valueFinder = ExpectedValuesFinder("../../resources/expectedValue.json")
    schemaType2Domains = {'table':[],'list':[],'text':[]}
    for dominio in os.listdir("../../input/"):
        print(dominio)
        pages4Detection = list(PageBroker().findHtmlFileWithPath("../../input/"+dominio,dominio))
        pages4Detection = pages4Detection[0:1]
        print(pages4Detection)
        detector.setInformationKeyword(PATH_KEYWORDS)
        schemaType=detector.detect(pages4Detection)
        schemaType2Domains[schemaType].append(dominio)
    print(schemaType2Domains)
    for dominio in schemaType2Domains['table']:
        for page in os.listdir("../../input/"+dominio):
            d = tableExtr.extractSpecificationsFromPage("../../input/"+dominio+"/"+page)
            print(d)
            tableExtr.saveSpecificationDictionaryAsJson(d, page, "../../input/"+dominio)
            valueFinder.updateExpectedValues(d)
