# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 20:42:52 2018

@author: bushra
"""

def mode (length_1,length_2,list1,list2):
    max_count = 0
    mode_list=[]
    merge_list=list1+list2
    sorted_list=sorted(merge_list)
    print("sorted lists=",sorted_list)
    length_sorted= len(sorted_list)
    for i in range(length_sorted):
        count=0
        for j in range(i,length_sorted):
            if merge_list[j]==merge_list[i]:
                count=count+1
                print("count=",count)
        if count>1:
            if count>max_count:
                max_count=count
                #print("max count=",max_count)
                mode_list.append(merge_list[i])
                #print("mod list=",mode_list)
                if mode_list[0]!="":
                    mode_list.pop(0)
                    mode_list.insert(0,merge_list[i])
                    #del mode_list[1]
            elif count==max_count:
                mode_list.append(merge_list[i])
        if i==(length_sorted-1):
            print("mode list=",mode_list)
    if(max_count==0):
        print("There is no mode for the data list")