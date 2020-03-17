# ======================================================
#  Packaging Python Projects Tutorial : https://packaging.python.org/tutorials/packaging-projects/ 
#
#  Installation : #  pip install -i https://test.pypi.org/simple/ utils-edchin
#
#
# ===================================================================


#  Importing
if __name__ == "__main__":
    import pandas
    df_in = pandas.DataFrame({"abbrev": ["OH", "MI", "SD", "PR", "PA"]})

    # import utils_edchin as edc
    # print (dir(edc.DataProcessor.add_state_names))
    # df_out = edc.DataProcessor.add_state_names(df_in=df_in)

    import utils_edchin.DataProcessor as dp
    print (dir(dp))
    df_out = dp.add_state_names(df_in=df_in)
    print('Output:\n', df_out.head()) 

