## Master Thesis
# Systemic Literature Review inspired by Kira

import pandas as pd
import numpy as np
import FunctionsLitRe as flr

### Get data from Excel and convert to Dataframe

## Scopus
#ScopRs1a_source = pd.read_csv('/Users/leonhardschonfelder/Desktop/02_Code/Research_02/Research_1a_scop.csv')
ScopRs1b_source = pd.read_csv('/Users/leonhardschonfelder/Desktop/02_Code/Research_02/Research_1b_scop.csv')
ScopRs1c_source = pd.read_csv('/Users/leonhardschonfelder/Desktop/02_Code/Research_02/Research_1c_scop.csv')
ScopRs1d_source = pd.read_csv('/Users/leonhardschonfelder/Desktop/02_Code/Research_02/Research_1d_scop.csv')
#ScopRs2a_source = pd.read_csv('/Users/leonhardschonfelder/Desktop/02_Code/Research_02/Research_2a_scop.csv')
ScopRs2b_source = pd.read_csv('/Users/leonhardschonfelder/Desktop/02_Code/Research_02/Research_2b_scop.csv')
ScopRs2c_source = pd.read_csv('/Users/leonhardschonfelder/Desktop/02_Code/Research_02/Research_2c_scop.csv')
ScopRs2d_source = pd.read_csv('/Users/leonhardschonfelder/Desktop/02_Code/Research_02/Research_2d_scop.csv')

## Web of Science
#WoSRs1a_source = pd.read_excel('/Users/leonhardschonfelder/Desktop/02_Code/Research_02/Research_1a_wos.xls')
#WoSRs1b_source = pd.read_excel('/Users/leonhardschonfelder/Desktop/02_Code/Research_02/Research_1b_wos.xls')
WoSRs1c_source = pd.read_excel('/Users/leonhardschonfelder/Desktop/02_Code/Research_02/Research_1c_wos.xls')
WoSRs1d_source = pd.read_excel('/Users/leonhardschonfelder/Desktop/02_Code/Research_02/Research_1d_wos.xls')
WoSRs2b_source = pd.read_excel('/Users/leonhardschonfelder/Desktop/02_Code/Research_02/Research_2b_wos.xls')
WoSRs2c_source = pd.read_excel('/Users/leonhardschonfelder/Desktop/02_Code/Research_02/Research_2c_wos.xls')
WoSRs2d_source = pd.read_excel('/Users/leonhardschonfelder/Desktop/02_Code/Research_02/Research_2d_wos.xls')

### Merge Research 1a and 1b
"""print("Rows_Scop1A:", len(ScopRs1a_source), "Columns_Scop1A:", len(ScopRs1a_source.columns))
print("Rows_Scop1B:", len(ScopRs1b_source), "Columns_Scop1b:", len(ScopRs1b_source.columns))
print()
print("Rows_WoS1A:", len(WoSRs1a_source), "Columns_WoS1A:", len(WoSRs1a_source.columns))
print("Rows_WoS1b:", len(WoSRs1b_source), "Columns_WoS1b:", len(WoSRs1b_source.columns))
print()"""

    # concat files

scop_con_R1 = (pd.concat([ScopRs1b_source, ScopRs1c_source,ScopRs1d_source])).sort_values(by='Title')
wos_con_R1 = (pd.concat([WoSRs1c_source, WoSRs1d_source])).sort_values(by='Article Title')

    # eliminate duplicats

scop_R1_new = scop_con_R1.drop_duplicates(subset = 'Title')
wos_R1_new = wos_con_R1.drop_duplicates(subset = 'Article Title')

"""print("Rows_Scop_new:", len(scop_R1_new), "Columns_Scop_new:", len(scop_R1_new.columns))
print("Rows_Scop_new:", len(wos_R1_new), "Columns_Scop_new:", len(wos_R1_new.columns))"""

### Merge Research 2a - 2d

    # concat files
scop_con_R2 = (pd.concat([ScopRs2b_source, ScopRs2c_source, ScopRs2d_source])).sort_values(by ='Title')
wos_con_R2 = (pd.concat([WoSRs2b_source, WoSRs2c_source, WoSRs2d_source])).sort_values(by ='Article Title')

    # eliminate duplicats
scop_R2_new = scop_con_R2.drop_duplicates(subset = 'Title')
wos_R2_new = wos_con_R2.drop_duplicates(subset = 'Article Title')

### Merge Files Scopus & WoS

    # drop non-necessary columns for selection
        # SCOPUS
pop_list_scop = flr.sort_columns_to_pop(scop_R1_new)[1]

scop_R1_sort_title = scop_R1_new.drop(columns = pop_list_scop)
scop_R2_sort_title = scop_R2_new.drop(columns = pop_list_scop)

flr.filesave(scop_R1_sort_title, 'ScopusR1_Step01', r'/Users/leonhardschonfelder/Desktop/02_Code/Research_02/')
flr.filesave(scop_R2_sort_title, 'ScopusR2_Step01', r'/Users/leonhardschonfelder/Desktop/02_Code/Research_02/')

        # Web of Science
pop_list_wos = flr.sort_columns_to_pop(wos_R1_new)[1]
wos_R1_sort_title = wos_R1_new.drop(columns = pop_list_wos)
wos_R2_sort_title = wos_R2_new.drop(columns = pop_list_wos)

    # Save files
flr.filesave(wos_R1_sort_title, 'WoSR1_Step01', r'/Users/leonhardschonfelder/Desktop/02_Code/Research_02')
flr.filesave(wos_R2_sort_title, 'WoSR2_Step01', r'/Users/leonhardschonfelder/Desktop/02_Code/Research_02')
