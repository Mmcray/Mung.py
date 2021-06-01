import pandas as pd
import os

path = ''
file_name = ''


class Mung:
    # "Because the data won't Mung itself"

    def __init__(self):
        self.path = os.getcwd() + '\\'
        self.file_name = input('File: ')

    def extension(self):
        available = {'.csv': pd.read_csv, '.xls': pd.read_excel, '.xlsx': pd.read_excel, '.html': pd.read_html}
        extension = self.file_name[-4:]
        print('Here is: ' + extension)
        self.read_extension = available.get(extension)
        print('I got ' + 'read_extension')

    def read_file(self):
        call_pandas = self.read_extension
        print(call_pandas)
        self.df = call_pandas(self.path + self.file_name)
        self.df.head()
        print("File has been loaded to Pandas.")

    def data_info(self):
        df = self.df
        data_description = df.describe()
        data_nulls = df.isna().sum()
        data_info = df.info()

        print('DataFrame Description:')
        print(data_description)
        print('DataFrame Info')
        print(data_info)
        print('Nulls')
        print(data_nulls)
