import pandas as pd
import os

path = ''
file_name = ''


class Mung:
    # "Because the data won't Mung itself"

    # Takes an input as the file to be loaded into Pandas and the current working directory for that file location
    def __init__(self):
        self.path = os.getcwd() + '\\'
        self.file_name = input('File: ')

    # Parse the extension from the inputed file to determine which to_ Pandas method to call
    def extension(self):
        available = {'.csv': pd.read_csv, '.xls': pd.read_excel, '.xlsx': pd.read_excel, '.html': pd.read_html}
        fname = self.file_name
        extension_sp = fname.split('.')
        extension = ('.' + str(extension_sp[1]))
        print('Extension to read is: ' + extension)
        self.read_extension = available.get(extension)

    # Loads the dataframe and saves it as 'df'
    def read_file(self):
        call_pandas = self.read_extension
        print(call_pandas)
        self.df = call_pandas(self.path + self.file_name)
        print("File has been loaded to Pandas.")
        return self.df

    # Pandas exploration methods
    def data_info(self):
        df = self.df
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
        return self.df

    def clean_nulls(self):
        nonulls = ['Yes', 'yes', 'YES', 'y', 'Y']
        question = input('Would you like to remove rows with Nulls (Yes or No)? ')
        df = self.df
        if question in nonulls:
            bynulls = df.dropna()
            print('Rows with Nulls have been removed. \n')
            print(bynulls)
        else:
            print('No rows will be dropped')
        return df

    def drop_cols(self):
        df = self.df
        col_lst_to_drop = []
        no_drop = ['N', 'n', 'none']
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
        df = df.drop(col_lst_to_drop, axis='columns', inplace=True)
        print('Done dropping columns')
        return df
