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

def test():
    print('Testf')

def validateages(dt,agecolumn):
    validages = dt[pd.to_numeric(dt[agecolumn], errors='coerce').notnull()]
    return validages

def groupages(dt,agecolumn,lower,upper):
    grouped = dt[(dt[agecolumn] >= lower) & (dt[agecolumn] <= upper)]
    grouped = grouped["How old are you?"] = grouped["How old are you?"].astype(float)
