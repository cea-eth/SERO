## Master Thesis
# Systemic Literature Review inspired by Kira

import pandas as pd
import numpy as np
import Functions_FoIP as flr

### Get data from Excel and convert to Dataframe

## ScopWoS
lit_R1 = pd.read_csv('/Users/leonhardschonfelder/Desktop/02_Code/Research/LitReview01_Step02.csv')
lit_R2 = pd.read_csv('/Users/leonhardschonfelder/Desktop/02_Code/Research/LitReview02_Step02.csv')

## Fill nan with 'No Abstract available'
lit_R1 = lit_R1.fillna(value = {'Abstract': 'No Abstract'})
lit_R2 = lit_R2.fillna(value = {'Abstract': 'No Abstract'})

print(len(lit_R1), len(lit_R1.columns))
print(len(lit_R2), len(lit_R2.columns))

### Sort Papers by Abstract & Write new Excel-File with Literature
lit_R1 = flr.choose_by_abstract(lit_R1, 'Abstract', 'Title')
flr.filesave(lit_R1, 'LitReview01_Step03',r'/Users/leonhardschonfelder/Desktop/02_Code/Research_02')

lit_R2 =flr.choose_by_abstract(lit_R2, 'Abstract', 'Title')
flr.filesave(lit_R2, 'LitReview02_Step03',r'/Users/leonhardschonfelder/Desktop/02_Code/Research_02')
