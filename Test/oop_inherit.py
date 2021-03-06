# (OOP approach w/ inheritance)
import pandas
class CustomFrame(pandas.DataFrame):
    """
    Param: my_df (pandas.DataFrame) containing a column called "abbrev"
    """
    def add_state_names(self):
        """
        
        Adds corresponding state names to a dataframe.
        """
        # type(new_df["abbrev"]) #> <class 'pandas.core.series.Series'>
        # see: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
        names_map = {
            "CA": "Cali",
            "CT": "Conn",
            "CO": "Colorado"
            # todo: more abbrevs!
        }
        self["name"] = self["abbrev"].map(names_map)
if __name__ == "__main__":
    print("--------------")
    custom_df = CustomFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC"]})
    print(custom_df.head())
    custom_df.add_state_names()
    print(custom_df.head())
