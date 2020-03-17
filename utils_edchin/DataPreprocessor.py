# utils_edchin/DataPreprocessor.py

import pandas
class DataProcessor():
    def __init__(self):
        """
        Param: 
        """

    def add_state_names(self, df_in):
        """
        Adds corresponding state names to a dataframe.
        Param: df_in (pandas.DataFrame) containing a column called "abbrev"
        """
        df_out = df_in.copy()
        # type(new_df["abbrev"]) #> <class 'pandas.core.series.Series'>
        # see: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
        names_map = {
            "CA": "Cali",
            "CT": "Conn",
            "CO": "Colorado",
            "TX": "Texas",
            "DC": "Washington DC"
            # todo: more abbrevs!
        }
        df_out["name"] = df_out["abbrev"].map(names_map)
        return df_out


if __name__ == "__main__":
    print("--------------")
    # setup sample dataframes
    df1 = pandas.DataFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC"]})
    df2 = pandas.DataFrame({"abbrev": ["OH", "MI", "CO", "TX", "PA"]})
    
    processor = DataProcessor() # instantiate object (pass in a dataframe)

    #  Process df1
    print('Input:\n', df1)  # verify input
    df_processed = processor.add_state_names(df1) # add names to the state abbrev's
    print('Output:\n', df_processed.head())  # verify output

    #  Process df2
    print('Input:\n', df2)  # verify input
    df_processed = processor.add_state_names(df2) # add names to the state abbrev's
    print('Output:\n', df_processed.head())  # verify output
