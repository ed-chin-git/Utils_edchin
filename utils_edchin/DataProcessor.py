# utils_edchin/DataPreprocessor.py

import pandas as pd
from collections import Counter

class DataProcessor():
    def __init__(self):
        """
            USE : 
            import utils_edchin.DataProcessor as dpro
            dpro = dpro()
            dpro.add_state_names(df1,column_name)
        """


    def add_state_names(self, df_in, abbrev_col):
        """
        Adds corresponding state names to a dataframe.
        Param: df_in (pd.DataFrame, column_name str) 
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
        df_out["name"] = df_out[abbrev_col].map(names_map)
        return df_out

    def word_count(self, docs):
        '''

        This function takes a list of tokenized documents as input and returns
        a dataframe with 
        
        # Arguments
            docs: list, tokenized list of documents
            
        # Returns
            wc: dataframe, 
        
        Reference:
        D:/Github/DSPT4/DS-Unit-4-Sprint-1-NLP/module1-text-data/LS_DSPT4_411_Text Data_Lecture.ipynb

        '''
        
        word_counts = Counter()
        appears_in = Counter()

        total_docs = len(docs)

        for doc in docs:
            word_counts.update(doc)
            appears_in.update(set(doc))

        temp = zip(word_counts.keys(), word_counts.values())

        wc = pd.DataFrame(temp, columns = ['word', 'count'])

        wc['rank'] = wc['count'].rank(method='first', ascending=False)
        total = wc['count'].sum()

        wc['pct_total'] = wc['count'].apply(lambda x: x / total)

        wc = wc.sort_values(by='rank')
        wc['cul_pct_total'] = wc['pct_total'].cumsum()

        t2 = zip(appears_in.keys(), appears_in.values())
        ac = pd.DataFrame(t2, columns=['word', 'appears_in'])
        wc = ac.merge(wc, on='word')

        wc['appears_in_pct'] = wc['appears_in'].apply(lambda x: x / total_docs)

        return wc.sort_values(by='rank')

if __name__ == "__main__":

    import utils_edchin.pyxlib as sysx
    sysx = sysx()
    sysx.clear_terminal()        
    
    import sys
    print ('Python version',sys.version)
    
    # python -m package.subpackage.module
    # setup sample dataframes
    df1 = pd.DataFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC"]})
    df2 = pd.DataFrame({"State": ["OH", "MI", "SD", "PR", "PA"]})
    
    processor = DataProcessor() # instantiate object
    
    #  Process df1
    print('Input:\n', df1.head())  # verify input
    df_processed = processor.add_state_names(df1,'abbrev') # add names to state abbrev's
    print('Output:\n', df_processed.head())  # verify output

    #  Process df2
    print('Input:\n', df2.head())  # verify input
    df_processed = processor.add_state_names(df2, 'State') # add names to state abbrev's
    print('Output:\n', df_processed.head())  # verify output

    df_wc = processor.word_count(df_processed['name'])
    print(df_wc)
