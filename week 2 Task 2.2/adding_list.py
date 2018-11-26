# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 20:55:03 2018

@author: bushra
"""

list1=[]
list2=[]
length_1=int(input("Enter the length of the list 1="))
length_2=int(input("Enter the length of the list 2="))
if(length_1<=0 or length_2<=0):
    print("The length of the list cannot be 0 or negative")
elif length_1==length_2:
    print ("Enter the numbers in the list 1=")
    for i in range(length_1):
        try:
            data_1=float(input())
            list1.append(data_1)
        except:
            continue
    print ("Enter the number in the list 2 =")
    for i in range(length_2):
        try:
            data_2=float(input())
            list2.append(data_2)
        except:
            continue
    print ("The numbers inserted in 1st lists are=",list1)
    print ("The numbers inserted in 2nd lists are=",list2)
    
    from module import mean
    c=mean (length_1,length_2,list1,list2)
    print c

    from module_median import median
    d=median(length_1,length_2,list1,list2)
    print d
    
    from module_mode import mode
    e=mode(length_1,length_2,list1,list2)
    print e
    
    from module_rmse import root_mean
    f=root_mean(length_1,length_2,list1,list2)
    print f
    
    from module_man_dis import manhattan
    g=manhattan(length_1,length_2,list1,list2)
    print g
else:
    print("The length of two lists should be same")
