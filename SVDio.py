# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 19:39:08 2019

@author: Álvaro García, Belén Serrano

"""

from scipy.io import loadmat

class SVDio:
    
    
    def __init__(self, filename):
        self.file = filename
    
    def importData(self):
        mnist = loadmat(self.file)
        #digits = mnist['data']
        return mnist['data']
    
    