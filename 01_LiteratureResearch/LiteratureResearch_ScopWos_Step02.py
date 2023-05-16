## Master Thesis
# Systemic Literature Review inspired by Kira

import pandas as pd
import numpy as np
import Functions_FoIP as flr

### Get data from Excel and convert to Dataframe

## Scopus
scop_R1 = pd.read_csv('/Users/leonhardschonfelder/Desktop/02_Code/Research_02/ScopusR1_Step01.csv')
scop_R2 = pd.read_csv('/Users/leonhardschonfelder/Desktop/02_Code/Research_02/ScopusR2_Step01.csv')

## Web of Science
wos_R1 = pd.read_csv('/Users/leonhardschonfelder/Desktop/02_Code/Research_02/WoSR1_Step01.csv')
wos_R2 = pd.read_csv('/Users/leonhardschonfelder/Desktop/02_Code/Research_02/WoSR2_Step01.csv')

    # Rename WoS Column title

wos_R1.rename(columns = {'Article Title' : 'Title'})
wos_R2.rename(columns = {'Article Title' : 'Title'})
"""print(len(wos_R2_new), len(wos_R2_new.columns))
print(len(scop_R2_new), len(scop_R2_new.columns))"""

    # concat DataFrames
lit_re_con_R1 = (pd.concat([scop_R1, wos_R1])).sort_values(by = 'Title')
lit_re_con_R2 = (pd.concat([scop_R2, wos_R2])).sort_values(by = 'Title')

"""print(len(lit_re_R1),len(lit_re_R1.columns))
print(len(lit_re_R2), len(lit_re_R2.columns))"""

    # Drop duplicates
lit_R1 = lit_re_con_R1.drop_duplicates(subset = 'Title')
lit_R2 = lit_re_con_R2.drop_duplicates(subset = 'Title')

    #Drop nan-entries in Title
lit_R1 = lit_R1.dropna(subset = 'Title')
lit_R2 = lit_R2.dropna(subset = 'Title')

"""print(len(lit_R1), len(lit_R1.columns))
print(len(lit_R2), len(lit_R2.columns))"""

### Sort Papers by Title and directly save the file
lit_re_R1_fin = flr.choose_by_title(lit_re_R1, 'Title')
flr.filesave(lit_re_R1_fin, 'LitReview01_Step02',r'/Users/leonhardschonfelder/Desktop/02_Code/Research_02')

lit_re_R2_fin = flr.choose_by_title(lit_re_R2, 'Title')
flr.filesave(lit_re_R2_fin, 'LitReview02_Step02',r'/Users/leonhardschonfelder/Desktop/02_Code/Research_02')


