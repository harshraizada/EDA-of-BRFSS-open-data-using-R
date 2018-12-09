#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 19:34:27 2018

@author: harsh
"""
# changing of working directory
import os
os.getcwd()
os.chdir(r"/Users/harsh/Desktop/Python programming course /pproject")
# importing of important packages for analysis
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#reading of data CSV file.
brfss=pd.read_csv("brfssp.csv")

#copy of main data set i.e brfss into another dataset.
cbrfss=brfss

#slicing & subsetting of data frame with selected variables.
cbrfssci=cbrfss[(cbrfss.DISPCODE==1100)]

## A. IMMUNIZATION COVERAGE STATUS

#Objective-1 To find out the existing coverage rate of Tetanus shot among US residents. 
tt=cbrfssci.TETANUS.value_counts()
tt1=tt.to_frame()
tt1["Percentage"]=round((tt1/tt1.sum())*100,2)
tt1["Category"]={"No, did't receive any TT since 2005":4.0,"Yes,not sure what type":3.0,"Yes,received Tdap":1.0,"Don't know":7.0,"Yes,got TT but not Tdap":2.0,"Refused":9.0}
ttbar=sns.barplot(data=tt1,x="Category",y="Percentage"\
                  ,palette="deep")
plt.axhline(0, color="k", clip_on=False)
plt.title("TT vaccination coverage in US population",fontsize=18)
plt.xlabel("Responses",fontsize=15)
plt.ylabel("Percentage",fontsize=15)
plt.ylim(0,50)
plt.xticks(rotation='vertical')
rects = ttbar.patches
for rect in rects:
    y_value = rect.get_height()
    x_value = rect.get_x() + rect.get_width() / 2
    space = 5
    va = 'bottom'
    label = "{:.1f}".format(y_value)
    plt.annotate(label,(x_value, y_value),xytext=(0, space),\
                 textcoords="offset points",ha='center',va=va)
plt.figure(figsize=(10,7)) 
  
#Objective-2 To find out the existing coverage rate of  Pneumococcal vaccine among US residents.
pcv=cbrfssci.PNEUVAC3.value_counts()
pcv1=pcv.to_frame()
pcv1["Percentage"]=round((pcv1/pcv1.sum())*100,2)
pcv1["Category"]={"No":2.0,"Yes":1.0,"Don't know":7.0,"Refused":9.0}
pcvbar=sns.barplot(data=pcv1,x="Category",y="Percentage",\
                   palette="vlag",)
plt.title("PCV coverage in US population",fontsize=18)
plt.xlabel("Responses",fontsize=15)
plt.ylabel("Percentage",fontsize=15)
plt.ylim(0,70)
rects = pcvbar.patches
for rect in rects:
    y_value = rect.get_height()
    x_value = rect.get_x() + rect.get_width() / 2
    space = 5
    va = 'bottom'
    label = "{:.1f}".format(y_value)
    plt.annotate(label,(x_value, y_value),xytext=(0, space),\
                 textcoords="offset points",ha='center',va=va)

## B.CHRONIC HEALTH CONDITION STATUS-ASTHMA

#Objective-3 To find out how much percentage of US residents ever told about asthma by their doctor.
astd=cbrfssci.ASTHMA3.value_counts()
astd1=astd.to_frame()
astd1["Percentage"]=round((astd1/astd1.sum())*100,2)
astd1["Category"]={"No":2.0,"Yes":1.0,"Don't know":7.0,"Refused":9.0}
astdbar=sns.barplot(data=astd1,x="Category",y="Percentage",\
                    palette="rocket",)
plt.title("Ever told by doctor about asthma",fontsize=18)
plt.xlabel("Responses",fontsize=15)
plt.ylabel("Percentage",fontsize=15)
plt.ylim(0,100)
rects = astdbar.patches
for rect in rects:
    y_value = rect.get_height()
    x_value = rect.get_x() + rect.get_width() / 2
    space = 5
    va = 'bottom'
    label = "{:.1f}".format(y_value)
    plt.annotate(label,(x_value, y_value),xytext=(0, space),\
                 textcoords="offset points",ha='center',va=va)

#Objective-4 Among those who ever told about asthma by doctor how many still have asthma? 
astdy=cbrfssci[(cbrfssci.ASTHMA3==1)]
asc=astdy.ASTHNOW.value_counts()
asc1=asc.to_frame()
asc1["Percentage"]=round((asc1/asc1.sum())*100,2)
asc1["Category"]={"Yes":1.0,"No":2.0,"Don't know":7.0,"Refused":9.0}
ascdbar=sns.barplot(data=asc1,x="Category",y="Percentage")
plt.title("Ever told by doctor about asthma and still have asthma",fontsize=18)
plt.xlabel("Responses",fontsize=15)
plt.ylabel("Percentage",fontsize=15)
plt.ylim(0,100)
rects = ascdbar.patches
for rect in rects:
    y_value = rect.get_height()
    x_value = rect.get_x() + rect.get_width() / 2
    space = 5
    va = 'bottom'
    label = "{:.1f}".format(y_value)
    plt.annotate(label,(x_value, y_value),xytext=(0, space),\
                 textcoords="offset points",ha='center',va=va)

#Objective-5 Among those who still have asthma how many had an episode of asthma or an asthma attack in past 12 months? 
ascy=cbrfssci[(cbrfssci.ASTHNOW==1)]
asat=ascy.ASATTACK.value_counts()
asat1=asat.to_frame()
asat1["Percentage"]=round((asat1/asat1.sum())*100,2)
asat1["Category"]={"No":2.0,"Yes":1.0,"Don't know":7.0,"Refused":9.0}
asatdbar=sns.barplot(data=asat1,x="Category",y="Percentage",\
                     palette="vlag")
plt.title("Still have asthma & faced asthma attack in past 12 months",fontsize=18)
plt.xlabel("Responses",fontsize=15)
plt.ylabel("Percentage",fontsize=15)
plt.ylim(0,70)
rects = asatdbar.patches
for rect in rects:
    y_value = rect.get_height()
    x_value = rect.get_x() + rect.get_width() / 2
    space = 5
    va = 'bottom'
    label = "{:.1f}".format(y_value)
    plt.annotate(label,(x_value, y_value),xytext=(0, space),\
                 textcoords="offset points",ha='center',va=va)

# C. BREAST & CERVICAL CANCER SCREENING STATUS

# Objective -6 To find out the existing  Breasts cancer screening rate among US residents.
bcf=cbrfssci[(cbrfssci.SEX==2)]
bcs=bcf.HADMAM.value_counts()
bcs1=bcs.to_frame()
bcs1["Percentage"]=round((bcs1/bcs1.sum())*100,2)
bcs1["Category"]={"Yes":1.0,"No":2.0,"Don't know":7.0,"Refused":9.0}
bcsbar=sns.barplot(data=bcs1,x="Category",y="Percentage")
plt.title("Mamogram test status in US population",fontsize=18)
plt.xlabel("Responses",fontsize=15)
plt.ylabel("Percentage",fontsize=15)
plt.ylim(0,100)
rects = bcsbar.patches
for rect in rects:
    y_value = rect.get_height()
    x_value = rect.get_x() + rect.get_width() / 2
    space = 5
    va = 'bottom'
    label = "{:.1f}".format(y_value)
    plt.annotate(label,(x_value, y_value),xytext=(0, space),\
                 textcoords="offset points",ha='center',va=va)
# 7. Objective-7 To find out the existing  Cervical cancer screening rate among US residents.
ccf=cbrfssci[(cbrfssci.SEX==2)]
ccs=ccf.HADPAP2.value_counts()
ccs1=ccs.to_frame()
ccs1["Percentage"]=round((ccs1/ccs1.sum())*100,2)
ccs1["Category"]={"Yes":1.0,"No":2.0,"Don't know":7.0,"Refused":9.0}
ccsbar=sns.barplot(data=ccs1,x="Category",y="Percentage")
plt.title("PAP test status in US population",fontsize=18)
plt.xlabel("Responses",fontsize=15)
plt.ylabel("Percentage",fontsize=15)
plt.ylim(0,100)
rects = ccsbar.patches
for rect in rects:
    y_value = rect.get_height()
    x_value = rect.get_x() + rect.get_width() / 2
    space = 5
    va = 'bottom'
    label = "{:.1f}".format(y_value)
    plt.annotate(label,(x_value, y_value),xytext=(0, space),\
                 textcoords="offset points",ha='center',va=va)
    
## D. HIV/AIDS TEST STATUS

# Object-8 To find out the existing HIV testing rate among US residents.
hivtst=cbrfssci.HIVTST6.value_counts()
hivtst1=hivtst.to_frame()
hivtst1["Percentage"]=round((hivtst1/hivtst1.sum())*100,2)
hivtst1["Category"]={"No":2.0,"Yes":1.0,"Don't know":7.0,"Refused":9.0}
hivtst1
hivbar=sns.barplot(data=hivtst1,x="Category",y="Percentage")
plt.title("HIV test status in US population",fontsize=18)
plt.xlabel("Responses",fontsize=15)
plt.ylabel("Percentage",fontsize=15)
plt.ylim(0,100)
rects = hivbar.patches
for rect in rects:
    y_value = rect.get_height()
    x_value = rect.get_x() + rect.get_width() / 2
    space = 5
    va = 'bottom'
    label = "{:.1f}".format(y_value)
    plt.annotate(label,(x_value, y_value),xytext=(0, space),\
                 textcoords="offset points",ha='center',va=va)













