# -*- coding: utf-8 -*-
"""
Created on Thu Jun 07 14:12:37 2018

@author: k005129
"""

from __future__ import unicode_literals
import pandas as pd

from pyutils.exceltable import load_workbook, ws_to_list
from  __builtin__ import any
from dateutil import parser
import re
from armylist.models import Competence

def updatecompCSV():
    with load_workbook("D:\gitChrono\chronopia\chronopia\Pycomp\Pycomp\comp.xlsx") as wb:
        sheet1 = wb["Feuil1"]
        for i,row in enumerate(sheet1.rows):   
            if i > 1:
                pk = row[7].value
                if pk:
                    print pk        
                    objComp = Competence.objects.get(pk=pk)
                    objComp.description = row[5].value
                    objComp.name = row[4].value 
                    objComp.save()
                    
            
updatecompCSV();