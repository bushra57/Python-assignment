# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 23:08:39 2018

@author: bushra
"""

def mean(length_1,length_2,list1,list2):
    add=0;
    for i in range(len(list1)):
            add=add+list1[i]
    for j in range(len(list2)):
        add=add+list2[j]
    print('Total sum=',add) 
    div=len(list1)+len(list2)
    print (div)
    result=add/div
    print('mean of the lists=',result)
        
   
