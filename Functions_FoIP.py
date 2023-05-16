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
def dict_rename(obj01,obj02):
    # creates dictionnary to rename columns of dataframes
    # key from obj01, value from obj02 - rename works from key to value

    if isinstance(obj01, pd.DataFrame):
        l01 = list(obj01.columns)
    elif isinstance(obj01, list):
        l01 = obj01

    if isinstance(obj02, pd.DataFrame):
        l02 = list(obj02.columns)
    elif isinstance(obj02, list):
        l02 = obj02

    dict_rename = {}

    dict_rename = {}
    for key in l01:
        for value in l02:
            dict_rename[key] = value
            l02.remove(value)
            break

    return dict_rename
def num_column(dataframe):
    df = dataframe

    for i in list(df.columns):
        df[i] = pd.to_numeric(df[i])

    return df
def extract_factor(DataFrame):
    # create list with factors to replace column header of dataframe with factors intead of long text
    df = DataFrame
    l_df = list(df.columns)
    l_df_r = []

    for i in l_df:
        if '[' in i:
            l_df_r.append(i.split('[')[1].strip()[:-1])
        else:
            continue

    return l_df_r
def prep_plot_df(DataFrame_origin,row_start,row_end,column_start,column_end):
    #rename
    dfo, rs, re, cs, ce = DataFrame_origin, row_start, row_end, column_start, column_end

    df_r = pd.DataFrame(dfo.iloc[rs:re, cs:ce])
    df_ex = extract_factor(df_r)
    df_dic = dict_rename(df_r,df_ex)
    df_r = df_r.rename(columns = df_dic)
    df_r = num_column(df_r)

    return df_r
def search_keyword(dataframe, keyword,):
    ## search for keywords in column to partition answers / questions
    # returns range with
    return
def sort_by_mean(df):
    df_index = df.mean().sort_values().index
    df = df[df_index]
    return df
def meanofdf (df):

    mean_value = []
    for j in df.columns:
        mean_value.append(df.loc[:,j].mean())

    df_c_list = list(df.columns)
    """df_n = []

    for i in range(0,len(df_c_list)):
        df_n.append(str(df_c_list[i]) + ' [' + str(round(mean_value[i],2)) + ']')"""

    df_n = pd.DataFrame(list(zip(df_c_list,mean_value)), columns = ['Name', 'mean'])

    return df_n
