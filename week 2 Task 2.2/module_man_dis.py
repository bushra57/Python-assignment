# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 12:06:46 2018

@author: bushra
"""

def manhattan (length_1,length_2,list1,list2):
    print("")
    print("Considering list 1 as X and list 2 as Y for finding predictive vale of Y")
    m=len(list1)
    n=len(list2)
    total_man_dis=0
    for i in range(m-1):
        man_dis=0
        for j in range(i+1,n): 
            man_dis = (abs(list1[i] - list1[j]) +
                        abs(list2[i] - list2[j]))
            total_man_dis=total_man_dis+man_dis
            print("distance between",(list1[i],list2[i]),(list1[j],list2[j]),man_dis)
        print("Total Manhattan distance of other points from",(list1[i],list2[i]),total_man_dis)
        print("")
        print("")
     