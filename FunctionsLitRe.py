import pandas as pd
import numpy as np

def sort_columns_to_pop(DataFrame):
    Df = DataFrame
    pop_list = []
    for i in list(Df):
        print(i)
        choice = input('keep column yes = 1 or no = 0?')
        while not (choice == '1' or choice == '0'):
            choice = input('keep column yes = 1 or no = 0?')
        if choice == '0':
            Df = Df.drop(columns = i)
            pop_list.append(i)
        else:
            continue

    return Df,pop_list
def choose_by_title(DataFrame, ColumnTitle_Title):
    #manually insert the name of the column in which the title is in
    clm = ColumnTitle_Title
    DF_selection = DataFrame

    removed_papers = 0
    kept_papers = 0

    for j,i in enumerate(DF_selection[clm]):
        print('Title: ','\033[1m', i, '\033[0m')
        answer = input('keep (yes =1; no =0?)')
        while not (answer == '1' or answer == '0'):
            answer = input('keep (yes =1; no =0)?')
        if answer == '0':
            DF_selection = DF_selection.drop(list(DataFrame.index)[j])
            removed_papers += 1
            print('Removed titles so far: ',removed_papers)
            print(len(DF_selection)-kept_papers,' more papers to go.\n' )
        elif answer == '1':
            kept_papers += 1
            print('Removed titles so far: ',removed_papers)
            print(len(DF_selection)-kept_papers,' more papers to go.\n' )
            continue

    return DF_selection
def choose_by_abstract(DataFrame, ColumnTitle_Abstract, ColumnTitle_Title):
    #manually insert the name of the column in which the abstract is in
    clm_abs = ColumnTitle_Abstract
    clm_ttl = ColumnTitle_Title
    DF_selection = DataFrame

    #Need for column 'Use for Thesis'
    if not {'Use in Thesis', 'Priority'}.issubset(DataFrame.columns):
        DataFrame['Use in Thesis'] = ''
        DataFrame['Priority'] = ''

    # iterate through
    removed_papers = 0
    kept_papers = 0

    for j,i in enumerate(DF_selection[clm_abs]):
        print('Abstract of','\033[1m', DF_selection[clm_ttl][j] ,'\033[0m',' : \n', i)
        answer = input('keep (yes =1; no =0?)')
        while not (answer == '1' or answer == '0'):
            answer = input('keep (yes =1; no =0)?')
        if answer == '0':
            DF_selection = DF_selection.drop(list(DataFrame.index)[j])
            removed_papers += 1
            print('Removed titles so far: ',removed_papers)
            print(len(DF_selection)-kept_papers,' more papers to go.\n' )
        if answer == '1':
            print('What to use the Paper for in Thesis?')
            thesis_use = str(input())
            print('Pirority? (1-3, 1 most important)')
            prio = input()
            DF_selection.at[j, 'Use for Thesis'] = thesis_use
            DF_selection.at[j, 'Priority'] = prio
            kept_papers += 1
            print('Removed titles so far: ',removed_papers)
            print(len(DF_selection)-kept_papers,' more papers to go.\n' )
            continue

    return DF_selection
def filesave(DataFrame,Filename,Path):

    if isinstance(Filename, str):
        filename = Filename
        path = Path + '/' + filename + '.csv'
        DataFrame.to_csv(path)
    else:
        filename = str(Filename)
        path = Path + '/' + filename + '.csv'
        DataFrame.to_csv(path)

    return print('DataFrame is written to csv File successfully.')
def add_to_file(DataFrame,Filename_insert_to,List_of_Titles_To_Add):
    pass
    return
