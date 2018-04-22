'''
Created on 22 apr 2018

@author: davideorlando
'''
import os


class PageBroker(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def findHtmlFile(self, path):
        lista = (os.listdir(path))
        s = set()
        for e in lista:
            if e.find(".html") != -1:
                s.add(e)
        return s

    def findHtmlFileWithPath(self,path,dominio):
        lista = (os.listdir(path))
        s = set()
        for e in lista:
            if e.find(".html") != -1:
                s.add("../../input/"+dominio+"/"+e)
        return s