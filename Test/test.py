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
    import utils_edchin.pyxlib as pyx

    print (dir(dp))
    print (dir(pyx))
    
    df_out = dp.add_state_names(dp, df_in)
    print('Output:\n', df_out.head()) 

    print(pyx.variance_edc(pyx, [5, 25, 99, 1325, 1125, 555, 6546, 888]))
    print(pyx.removeOutliers(pyx, [-10, 2, 5, 3, 8, 4, 7, 5, 10, 99, 1000]))
