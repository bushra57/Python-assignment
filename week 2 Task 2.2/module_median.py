# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 11:26:18 2018

@author: bushra
"""

def median (length_1,length_2,list1,list2):
    merge_list=list1+list2
    sorted_list=sorted(merge_list)
    print("sorted lists=",sorted_list)
    length_sorted= len(sorted_list)
    if(length_sorted % 2==0):
        med= ((sorted_list[length_sorted/2] + sorted_list[length_sorted/2 - 1]) / 2.0)
        print("The median of the lists are=",med)
    else:
        print("The median of the lists are=",sorted_list[length_sorted/2])
        
        