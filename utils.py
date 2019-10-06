import pandas as pd
import datetime
import numpy as np


FY_START_MONTH = '-07-01 00:00:00'
FY_END_MONTH = '-06-30 00:00:00'

ALL = 'ALL'


def create_fy_columns(df, fy_dict, col_name):
    '''
    Creates binary columns that identify if a record was created within a given fiscal year
    
    Inputs:
        df: dataframe
        FY_DICT: dictionary created above that identifies the date range for each fiscal year since FY 2016
        col_name (str): name of column used to identify if a record occured in the given fiscal year
    
    Returns:
        df: dataframe with binary columns
    '''
    
    df[col_name] = pd.to_datetime(df[col_name])
    for key,val in fy_dict.items():
        start = val[0]
        end = val[1]
        df[key] = np.where(((df[col_name] >= start) & (df[col_name] <= end)), 1, 0)
        if datetime.datetime.now().year + 1 == end.year:
            fy_total_key = 'As of Today'
            print('true')
        else:
            fy_total_key = 'End_of_' + key
        df[fy_total_key] = np.where((df[col_name] <= end), 1, 0)
    
    return df


def build_fy_dictionary(df, col_name):
    print('its working still for sure foo0000oor sure')
    fy_dict = {}
    fy_filter_list = []
    for year in np.sort(df[col_name].dt.year.unique()):
        yr = int(year)
        start = str(yr) + FY_START_MONTH
        end_yr = yr + 1
        end = str(end_yr) + FY_END_MONTH
        key = 'FY_' + str(end_yr)
        fy_dict[key] = [pd.to_datetime(start), pd.to_datetime(end)]
        if datetime.datetime.now().year + 1 == end_yr:
            filter_key = 'As of Today'
        else:
            filter_key = 'End_of_' + key
        fy_filter_list.append(filter_key)

    return fy_dict, fy_filter_list


# clean date columns

def date_transformation(df, col_name):
    
    df[col_name] = pd.to_datetime(df[col_name])
    
    return df


def unique_sorted_values_plus_ALL(array, all=True):
    unique = array.unique().tolist()
    unique.sort()
    if all:
        unique.insert(0, ALL)
    return unique