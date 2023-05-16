import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
