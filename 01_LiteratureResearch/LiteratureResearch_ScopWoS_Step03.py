import pandas as pd
import numpy as np
from os.path import realpath, dirname, join
import Functions_FoIP as foip

### Get data from Excel and convert to Dataframe
folder_path = dirname(realpath(__file__))

## ScopWoS
lit_R1 = pd.read_csv(join(folder_path,'Research_02/LitReview01_Step02.csv'))
lit_R2 = pd.read_csv(join(folder_path,'Research_02/LitReview02_Step02.csv'))

## Fill nan with 'No Abstract available'
lit_R1 = lit_R1.fillna(value = {'Abstract': 'No Abstract'})
lit_R2 = lit_R2.fillna(value = {'Abstract': 'No Abstract'})

print(len(lit_R1), len(lit_R1.columns))
print(len(lit_R2), len(lit_R2.columns))

### Sort Papers by Abstract & Write new Excel-File with Literature
lit_R1 = foip.choose_by_abstract(lit_R1, 'Abstract', 'Title')
foip.filesave(lit_R1, 'LitReview01_Step03',join(folder_path,'Research_02'))

lit_R2 =foip.choose_by_abstract(lit_R2, 'Abstract', 'Title')
foip.filesave(lit_R2, 'LitReview02_Step03',join(folder_path,'Research_02'))
