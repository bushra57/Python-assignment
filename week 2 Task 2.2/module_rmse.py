# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 01:02:54 2018

@author: bushra
"""

def root_mean (length_1,length_2,list1,list2):
   y_pred=[]
   error_list=[]
   X=[]
   Y=[]
   m=len(list1)
   n=len(list2) 
   SS=0
   SP=0
   add_list1=0
   add_list2=0
   sqr_list1=0
   sqr_list2=0
   sqr_error=0
   #linear regression equation Y=a+bX
   #need to find value of a and b.then we will get predictive y from eqaution
   
   print("Considering list 1 as X and list 2 as Y for finding predictive vale of Y")
   #assuming list 1 as x
   for i in range(m):
       add_list1=add_list1+list1[i]
       sqr_list1=sqr_list1+list1[i]**2
   print("sum of X=",add_list1)
   print("sum of X^2=",sqr_list1)
    
    #assuming list 2 as y
   for i in range(n):
       add_list2=add_list2+list2[i]
       sqr_list2=sqr_list2+list2[i]**2
   
   print("sum of Y=",add_list2)
   print("sum of Y^2=",sqr_list2)
   
   mean_x=add_list1/m
   mean_y=add_list2/n
   print("mean of X=",mean_x)
   print("mean of Y=",mean_y)
   
   #calculating X-MX
   for i in range(m):
       X_MX=list1[i]-mean_x
       X.append(X_MX)
   for i in range(m):
       SS=SS+(X[i]**2)
   print("SS=",SS)

    #calculating (X-MX)(Y-MY)
   for i in range(m):
       Y_MY=list2[i]-mean_y
       Y.append(Y_MY)
   for i in range(n):
        SP=SP+(X[i]*Y[i])
   print("SP=",SP)
    
   #calculating b for linear regression
   b=(SP/SS)
   print("the value of b=",b)
   
   #calculating a for linear regression
   
   a=mean_y-b*mean_x
   print("the value of a=",a)
   
   #Find the predictive value of Y'
   for i in range(m):
      data_pred_y=a+b*list1[i] 
      y_pred.append(data_pred_y)
   print("List of predictive Y'=",y_pred)   
   print("")
   print("")
  
   #find the error Y-Y'
   for i in range(m):
      data_error=list2[i]-y_pred[i]
      error_list.append(data_error)
   print("The error of Y-Y'=",error_list)
   print("")
   print("")   
    #square the error
   for i in range(m):
       sqr_error=sqr_error+error_list[i]**2
   print("summation of squared error=",sqr_error)
   print("")
   print("") 
    #root mean square error
   rmse=(sqr_error/m)**(1.0/2)
   print("Root mean square error of the list=",rmse)
        
    
    
   
   