# -*- coding: utf-8 -*-
"""
Created on Thu Jun 07 14:12:37 2018

@author: k005129
"""

from __future__ import unicode_literals




from armylist.models import Competence,Unit

def updatecompCSV():
    with load_workbook("D:\gitChrono\chronopia\chronopia\Pycomp\Pycomp\comp.xlsx") as wb:
        sheet1 = wb["Feuil1"]
        for i,row in enumerate(sheet1.rows):   
            if i > 1:
                pk = row[7].value
                if pk:
                           
                    objComp = Competence.objects.get(pk=pk)
                    objComp.description = row[5].value
                    objComp.name = row[4].value 
                    objComp.save()
                    
def mergeP1P2(p1,p2):
    objComp = Competence.objects.get(pk=p1)
    
    objComp2 = Competence.objects.get(pk=p2)
    
    for c in objComp.units.all():
        objComp2.units.add(c)
    objComp.units.clear()
    objComp.delete()
    objComp2.save()
  #meute , tir en mélée
def deleteDouble():
    lst =[ 
          (1133,1113),
          (1193,1129),
          (1285,1275),#Botte secrète (x2)
          (1157,1147),
          (1134,1128),
          (1233,1116),
          (1238,1140),
          (1283,1277),
          (1254,1165),
          (1155,1110),
          (1159,1145),
          (1123,1119),
          (1149,1137),
          (1197,1152),
          (1292,1291),
          (1203,1114),
          (1274,1109),
          (1148,1126),
          (1168,1135),
          (1214,1118),
          (1186,1164)
	#(1243,1267),
	#(1248,1269),
    #(1115,1275),
    #(1199,1305),
    #(1219,1280),
    #(1250,1271),
    #(1189,1293),
    #(1221,1296),
    #(1195,1303),
    #(1213,1308),
    #(1228,1298),
    #(1198,1304),
    #(1171,1288),
    #(1242,1266),
    
    
    ]
    for pk1,pk2 in lst:
        mergeP1P2(pk1,pk2)
deleteDouble()