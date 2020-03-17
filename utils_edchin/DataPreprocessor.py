# utils_edchin/DataPreprocessor.py

import pandas

class DataProcessor():
    def __init__(self):
        """
        Param :
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
            "AL": "Alabama",
            "AK": "Alaska",
            "AZ": "Arizona",
            "AR": "Arkansas",
            "CA": "California",
            "CO": "Colorado",
            "CT": "Connecticut",
            "DE": "Delaware",
            "FL": "Florida",
            "GA": "Georgia",
            "HI": "Hawaii",
            "ID": "Idaho",
            "IL": "Illinois",
            "IN": "Indiana",
            "IA": "Iowa",
            "KS": "Kansas",
            "KY": "Kentucky",
            "LA": "Louisiana",
            "ME": "Maine",
            "MD": "Maryland",
            "MA": "Massachusetts",
            "MI": "Michigan",
            "MN": "Minnesota",
            "MS": "Mississippi",
            "MO": "Missouri",
            "MT": "Montana",
            "NE": "Nebraska",
            "NV": "Nevada",
            "NH": "New Hampshire",
            "NJ": "New Jersey",
            "NM": "New Mexico",
            "NY": "New York",
            "NC": "North Carolina",
            "ND": "North Dakota",
            "OH": "Ohio",
            "OK": "Oklahoma",
            "OR": "Oregon",
            "PA": "Pennsylvania",
            "RI": "Rhode Island",
            "SC": "South Carolina",
            "SD": "South Dakota",
            "TN": "Tennessee",
            "TX": "Texas",
            "UT": "Utah",
            "VT": "Vermont",
            "VA": "Virginia",
            "WA": "Washington",
            "WV": "West Virginia",
            "WI": "Wisconsin",
            "WY": "Wyoming",
            "DC": "District of Columbia",
            "MH": "Marshall Islands",
            "AE": "Armed Forces Africa",
            "AA": "Armed Forces Americas",
            "AE": "Armed Forces Canada",
            "AE": "Armed Forces Europe",
            "AE": "Armed Forces Middle East",
            "AP": "Armed Forces Pacific",
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
