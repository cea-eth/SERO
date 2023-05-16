import pandas
import pandas as pd
import glob
import os
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from os.path import realpath, dirname, join
import Functions_FoIP as foip

#------- Goal 1 -------
# analyze which factors have been chosen and how often, which have been discarded?
# translate results (fr --> german and afterwards ger --> eng)
# load all files throw in list or df and count amount of same factors
# create plot for factors (x-axis how often chosen; y-axis factor) using excel

# ----- File Load -----
folder_path = dirname(realpath(__file__))

dir =os.chdir(join(folder_path,'Results_Interview/Results_all'))
files_path = [os.path.abspath(x) for x in os.listdir()]

#list of all classes
classes_df_de = pd.read_csv(join(folder_path,'Results_Interview/Classes_all/IC2_allClasses_de.csv'), index_col = 0, header = None)
classes_df_en = pd.read_csv(join(folder_path,'Results_Interview/Classes_all/IC2_allClasses_en.csv'), index_col = 0, header = None)

#list of all factors
factors_df_de = pd.read_csv(join(folder_path,'Results_Interview/Factors_all/IC2_allFactors_de.csv'), index_col = 0, header = None)
factors_df_en = pd.read_csv(join(folder_path,'Results_Interview/Factors_all/IC2_allFactors_en.csv'), index_col = 0, header = None)

# iterate over path to open files
csv_file = []
for file in glob.glob("*.csv"):
    csv_file.append(file)

# ----- concat files to one df -----
li01 = []
for filename in csv_file:
    df = pd.read_csv(filename, index_col=None, header = None)
    li01.append(df)

frame = pd.concat(li01, axis=1, ignore_index=False)


# ----- Counting how often factors were named -----
counts = frame.apply(pd.Series.value_counts)

# merged_counts = pd.concat(counts, axis =1)
final_counts = counts.sum(axis =1)
final_counts = final_counts.sort_values(ascending = False)

# make dataframe out of series
final_counts = final_counts.to_frame()

# Drop all classes from dataframe
final_counts = final_counts.drop(index = classes_df_de.index)

# Print final Dataframe
#print(final_counts)

#translate results from de to eng
fdd = list(factors_df_de.index)
fde = list(factors_df_en.index)

dict_rename = {}
for key in fdd:
    for value in fde:
        dict_rename[key] = value
        fde.remove(value)
        break

final_counts = final_counts.rename(index = dict_rename)

print(final_counts)
# ----- save file -----
foip.filesave(final_counts,'Interview_Final_Results_en',join(folder_path,'Results_Interview'))
