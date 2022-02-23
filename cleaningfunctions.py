import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def numberofNAs(dt):
    NAs = dt.isna().sum()
    for num in range(len(dt.isna().sum())):
        print(NAs.keys()[num],NAs[num])
    return 

def validateages(dt,agecolumn):
    validages = dt[pd.to_numeric(dt[agecolumn], errors='coerce').notnull()]
    validages[agecolumn] = validages[agecolumn].astype(float)
    return validages

def groupages(dt,agecolumn,lower,upper):
    dt[agecolumn] = dt[agecolumn].astype(float)
    grouped = dt[(dt[agecolumn] >= lower) & (dt[agecolumn] <= upper)]
    return grouped

def findoutliers(dt,agecolumn): 
    zscores = dt[agecolumn].to_frame()
    zscores['z_score']=stats.zscore(zscores[agecolumn])
    zscores.loc[zscores['z_score'].abs()>3]
    return zscores.loc[zscores['z_score'].abs()>3]

def joypercentages(dt):
    listofpercents = []
    joytotal = 0
    joyanddespairtotal = 0
    for i in range(3,96):
        filler = dt[dt.columns[i]].dropna()
        try: # An KeyError happens when .value_counts()['JOY'] = 0 since it doesn't exist
            joyspercent = filler.value_counts()["JOY"]/sum(filler.value_counts())
            joytotal += filler.value_counts()["JOY"]
        except:
            joyspercent = 0
            joytotal += 0
        joyanddespairtotal += sum(filler.value_counts())
        listofpercents.append(joyspercent)
        print(dt.columns[i],joyspercent)
        print(filler.value_counts())
        print()
    return joytotal/joyanddespairtotal
