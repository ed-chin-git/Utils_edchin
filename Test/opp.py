# (OOP approach)
import pandas
class DataProcessor():
    def __init__(self, my_df):
        """
        Param: my_df (pandas.DataFrame) containing a column called "abbrev"
        """
        self.df = my_df.copy()
    def add_state_names(self):
        """
        Adds corresponding state names to a dataframe.
        Param: my_df (pandas.DataFrame) containing a column called "abbrev"
        """
        #new_df = self.df.copy()
        # type(new_df["abbrev"]) #> <class 'pandas.core.series.Series'>
        # see: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
        names_map = {
            "CA": "Cali",
            "CT": "Conn",
            "CO": "Colorado"
            # todo: more abbrevs!
        }
        self.df["name"] = self.df["abbrev"].map(names_map)
if __name__ == "__main__":
    print("--------------")
    df1 = pandas.DataFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC"]})

    processor = DataProcessor(df1)
    print(processor.df.head())
    processor.add_state_names()
    print(processor.df.head())
