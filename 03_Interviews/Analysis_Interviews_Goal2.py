# ----- IMPORTS -----
# for data processing
import pandas as pd
import numpy as np
# for import of files
import glob2
import os
import chardet
from pathlib import Path
# for visualizing
import matplotlib.pyplot as plt
import seaborn as sns
# own
import functions_results_survey as frs

#------- Goal 2 -------
# analyze which factors have been assigned to which classes
# translate results
# load files
# create metric with all classes chosen by the participants as columns
# same metric, assign factors to columns (classes)
# count doubles per column
# create plot per class - how often was class chosen?
# create plot for factors - how often was factor assigned to which class (table - columns = classes, rows = factors,
# cells = #how often factor in class --> sort from up left high to down right low (heat map!)

# File Load
index_df = pd.read_csv(r'/Users/leonhardschonfelder/Downloads/Results_Interview/Factors_all/IC2_allFactors_de_2.csv', index_col = 0, header = None) # list of all factors index_col = 'Index_Column_Name'
column_df_de = pd.read_csv(r'/Users/leonhardschonfelder/Downloads/Results_Interview/Classes_all/IC2_allClasses_de_2.csv', index_col = 0, header = None) #list of all classes index_col = 'Columns_Column_Name'

# create df with classes as columns and factors as indexes
res_fin = pd.DataFrame(index = index_df.index, columns = column_df_de.index)
res_fin = res_fin.fillna(0)
column_names = res_fin.columns

# Define the directory where the CSV files are stored
directory = r'/Users/leonhardschonfelder/Downloads/Results_Interview/Results_Classes'

# Iterate over each file in the directory
for filename in os.listdir(directory):

    # Load the CSV file into a dataframe
    filepath = os.path.join(directory, filename)

    # load CSV file into a byte string
    with open(filepath, 'rb') as f:
        rawdata = f.read()

    # Detect the encoding of the byte string (Problem: not all csv-files are/ could be read as in UTF-8 format)
    result = chardet.detect(rawdata)
    encoding = result['encoding']

    # load CSV file
    temp_df = pd.read_csv(filepath, encoding=encoding)


    # get column names
    temp_clmname = temp_df.columns[0]

    # get data
    temp_data = temp_df[temp_clmname]

    # iterate through data
    for dat in temp_data:
        res_fin.loc[dat,temp_clmname] += 1


# sort the columns according to the sum of their values
res_fin = res_fin[sorted(res_fin.columns, key=lambda x: res_fin[x].sum(), reverse=True)]

# Print the final dataframe
#print(res_fin)

# ----- Translate de - eng ------
"""ind_d = list(index_df.index)
ind_en = list(factors_df_en.index)

cl_d = column_names
cl_en = 

dict_rename = {}
for key in fdd:
    for value in fde:
        dict_rename[key] = value
        fde.remove(value)
        break

res_fin = res_fin.rename(index = dict_rename)"""

# ----- save file -----
path_save = r'/Users/leonhardschonfelder/Downloads/Results_Interview'
frs.filesave(res_fin, 'HeatMap_en', path_save)

# ----- Plot results -----
# --- Plot Prepare ---
idx_res_fin = res_fin.index
column_names = column_names

#
plt.figure(figsize=(8, 6))

# Let the horizontal axes labeling appear on top.
# set x-axis labels to top
plt.gca().xaxis.tick_top()
plt.gca().xaxis.set_label_position('top')
plt.xticks(rotation=45)
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False, labeltop=True)

sns.heatmap(res_fin, cmap='Blues', vmin=res_fin.values.min(), vmax=res_fin.values.max(), annot=False, fmt='.0f')
plt.show()
