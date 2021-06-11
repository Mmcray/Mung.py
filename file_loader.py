import pandas
import pandas as pd
import os

path = os.getcwd() + '\\'
file_name = input('File: ')


# Parse the extension from the inputed file to determine which to_ Pandas method to call
def read_file():
    available = {'.csv': pd.read_csv, '.xls': pd.read_excel, '.xlsx': pd.read_excel, '.html': pd.read_html}
    fname = file_name
    extension_sp = fname.split('.')
    exten = ('.' + str(extension_sp[1]))
    print('Extension to read is: ' + exten)
    read_extension = available.get(exten)
    # Loads the dataframe and saves it as 'df'
    call_pandas = read_extension
    df = call_pandas(path + file_name)
    print("File has been loaded to Pandas.")
    return df


df_r = read_file()


# Pandas exploration methods
def data_info():
    df = df_r
    data_head = df.head()
    data_description = df.describe()
    data_nulls = df.isna().sum()
    data_info = df.info(verbose=True)
    data_uniq = df.nunique(axis=0)

    print('\n First 5 rows:')
    print(data_head)
    print('\n DataFrame Description: ')
    print(data_description)
    print('\n DataFrame Info: ')
    print(data_info)
    print('\n Nulls: ')
    print(data_nulls)
    print('\n Unique values per column:')
    print(data_uniq)


def drop_cols():
    col_lst_to_drop = []
    no_drop = ['N', 'n', 'none']
    df = df_r
    col_lst = df.columns
    for col in col_lst:
        to_drop = input("List columns you'd like to drop one at a time. Input 'N' when done: ")
        if to_drop in no_drop:
            break
        elif to_drop in col_lst:
            col_lst_to_drop.append(to_drop)
            continue
        else:
            print('Column not in dataframe, please try again.')
            continue
    dfd = df.drop(col_lst_to_drop, axis=1, inplace=False)
    print('Done dropping columns')
    print(col_lst_to_drop)
    print(df.head())
    print(dfd)
    print(dfd.head())
    return dfd


def clean_nulls(dfd):
    no_nulls = ['Yes', 'yes', 'YES', 'y', 'Y']
    question = input('Would you like to remove rows with Nulls (Yes or No)? ')
    if question in no_nulls:
        df_dropped = dfd.dropna()
        print('Rows with Nulls have been removed. \n')
    else:
        df_dropped = dfd
        print('No rows will be dropped')
    dfdn = df_dropped
    return dfdn
