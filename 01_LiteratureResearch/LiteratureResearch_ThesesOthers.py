import pandas as pd
import numpy as np
from os.path import realpath, dirname, join
import Functions_FoIP as foip

### Get data from Excel and convert to Dataframe
folder_path = dirname(realpath(__file__))

"""### Get data from Excel and convert to Dataframe

other_source = pd.read_excel(join(folder_path,'Research/Lit_Review.xlsx'), sheet_name= 'Summary')

#Drop duplicates
other_source = other_source.drop_duplicates(subset = 'Title')

#Drop nan-entries in Title
other_source = other_source.dropna(subset = 'Title')

#Search by Title
other_source_fin = foip.choose_by_title(other_source, 'Title')
foip.filesave(other_source_fin, 'Other_Sources_Step02')"""

#Search by Abstract
other_source_abs = pd.read_csv(join(folder_path,'Research/Other_Sources_Step02.csv'))

## Fill nan with 'No Abstract available'
other_source_abs = other_source_abs.fillna(value = {'Abstract Note': 'No Abstract'})

## Insert new column "USE in Thesis" for the possible use of the paper in the thesis
other_source_abs['Use in Thesis'] = ''
other_source_abs['Priority'] = ''

### Sort Papers by Abstract
other_source_abs_fin = foip.choose_by_abstract(other_source_abs, 'Abstract Note', 'Title')

### Write new Excel-File with Literature
# writing to csv
foip.filesave(other_source_abs_fin, 'Other_Sources_Step03',join(folder_path,'Research'))
