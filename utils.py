import pandas as pd
import datetime
import numpy as np


FY_DICT = {
    'fy_16': [pd.to_datetime('2015-07-01 00:00:00'), pd.to_datetime('2016-06-30 00:00:00')],
    'fy_17': [pd.to_datetime('2016-07-01 00:00:00'), pd.to_datetime('2017-06-30 00:00:00')],
    'fy_18': [pd.to_datetime('2017-07-01 00:00:00'), pd.to_datetime('2018-06-30 00:00:00')],
    'fy_19': [pd.to_datetime('2018-07-01 00:00:00'), pd.to_datetime('2019-06-30 00:00:00')],
    'fy_20': [pd.to_datetime('2019-07-01 00:00:00'), pd.to_datetime('2020-06-30 00:00:00')]
}

def create_fy_columns(df, col_name):
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
    
    for key,val in FY_DICT.items():
        start = val[0]
        end = val[1]
        df[key] = np.where(((df[col_name] >= start) & (df[col_name] <= end)), 1, 0)
        df['until_' + key] = np.where((df[col_name] <= end), 1, 0)
    
    return df

# filter for Fiscal Year 2019

def apply_date_mask(df, col_name, fy=True, 
                    start_date='2018-07-01 00:00:00', end_date='2019-06-30 00:00:00'):
    
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    
    if fy:
        mask = (df[col_name] >= start_date) & (df[col_name] <= end_date)
    else:
        mask = df[col_name] <= end_date
        
    df = df.loc[mask]
    
    return df

# clean date columns

def date_transformation(df, col_name):
    
    df[col_name] = pd.to_datetime(df[col_name])
    
    return df