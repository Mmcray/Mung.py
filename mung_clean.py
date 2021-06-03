from file_loader import Mung


class MungItClean(Mung):
    #df_tc = MungItClean.data_info()

    def __init__(self):
        self.self = self.Mung

    def remove_nulls(self):
        self.df_clean = Mung.df
        print(df)


print(dir(MungItClean))
print(MungItClean.data_info)
