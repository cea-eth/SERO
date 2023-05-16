## Master Thesis
# Systemic Literature Review inspired by Kira

import pandas as pd
import numpy as np
import FunctionsLitRe as flr

"""### Get data from Excel and convert to Dataframe

other_source = pd.read_excel('/Users/leonhardschonfelder/Desktop/02_Code/Research/Lit_Review.xlsx', sheet_name= 'Summary')

#Drop duplicates
other_source = other_source.drop_duplicates(subset = 'Title')

#Drop nan-entries in Title
other_source = other_source.dropna(subset = 'Title')

#Search by Title
other_source_fin = flr.choose_by_title(other_source, 'Title')
flr.filesave(other_source_fin, 'Other_Sources_Step02')"""

#Search by Abstract
other_source_abs = pd.read_csv('/Users/leonhardschonfelder/Desktop/02_Code/Research/Other_Sources_Step02.csv')

## Fill nan with 'No Abstract available'
other_source_abs = other_source_abs.fillna(value = {'Abstract Note': 'No Abstract'})

## Insert new column "USE in Thesis" for the possible use of the paper in the thesis
other_source_abs['Use in Thesis'] = ''
other_source_abs['Priority'] = ''

### Sort Papers by Abstract
other_source_abs_fin = flr.choose_by_abstract(other_source_abs, 'Abstract Note', 'Title')

### Write new Excel-File with Literature
# writing to csv
flr.filesave(other_source_abs_fin, 'Other_Sources_Step03')
