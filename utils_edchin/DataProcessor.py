# utils_edchin/DataPreprocessor.py

import pandas

class DataProcessor():
    def __init__(self):
        """
                # --- PREVIOUS VERSION ---
                # -- define class
                class = DataProcessor(df1)
                    def __init__(self, my_df):
                        self.df = my_df.copy()
                        return
                    def another_function()
                        new_df = self.df.copy()
                        return
                # -- instantiate obj
                processor = DataProcessor(df1) # class attribute holds df

        Input Params : none
        Sample call : processor = DataProcessor()
                      df_out = processor.add_state_names(df_in)
        """
        return

    def add_state_names(self, df_in):
        """
        Adds corresponding state names to a dataframe.
        Param: df_in (pandas.DataFrame) containing a column called "abbrev"
        """
        df_out = df_in.copy()
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
            "PR": "Puerto Rico",
            "AE": "Armed Forces Africa",
            "AA": "Armed Forces Americas",
            "AE": "Armed Forces Canada",
            "AE": "Armed Forces Europe",
            "AE": "Armed Forces Middle East",
            "AP": "Armed Forces Pacific",
    	 	"AS": "American Samoa",
	        "GU": "Guam",
            "MH": "Marshall Islands",
            "FM": "Micronesia",
            "MP": "Northern Marianas",
            "PW": "Palau",
            "VI": "Virgin Islands"
        }
        df_out["name"] = df_out["abbrev"].map(names_map)
        return df_out

def add_state_name(df_in):
    processor = DataProcessor()
    df_out = processor.add_state_names(df_in)
    return df_out


if __name__ == "__main__":
    # python -m package.subpackage.module
    # setup sample dataframes
    df1 = pandas.DataFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC"]})
    df2 = pandas.DataFrame({"abbrev": ["OH", "MI", "SD", "PR", "PA"]})
    
    # processor = DataProcessor() # instantiate object (pass in a dataframe)

    #  Process df1
    df_processed = add_state_name(df1) # add names to the state abbrev's
    print('Output:\n', df_processed.head())  # verify output

