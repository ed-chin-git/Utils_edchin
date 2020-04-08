# ======================================================
#  Packaging Python Projects Tutorial : https://packaging.python.org/tutorials/packaging-projects/ 
#
#  Installation : #  pip install -i https://test.pypi.org/simple/ utils-edchin
#
#
# ===================================================================


#  Importing
if __name__ == "__main__":
    ''' -- Run tests --
    '''
    import utils_edchin.pyxlib as edc_xlib # import class
    pyx = edc_xlib() # create instance
    print( pyx.variance_edc([5, 25, 99, 1325, 1125, 555, 6546, 888]))
    num_list = [-10, 2, 5, 3, 8, 4, 7, 5, 10, 99, 1000]
    print('List :', num_list)
    print('     :', type(num_list))
    print('Outliers :', pyx.listOutliers(num_list))
    print('wo/Outliers :', pyx.removeOutliers(num_list))
    print('TURBO reversed =', pyx.str_reverse('TURBO'))
    
    import pandas 
    import utils_edchin.DataProcessor as edc_dp # import class
    dp = edc_dp() # create instance
    df_in = pandas.DataFrame({"abbrev": ["OH", "MI", "SD", "PR", "PA"]})
    df_out = dp.add_state_names(df_in) # use it
    print('Input:\n', df_in.head())
    print('Output:\n', df_out.head())
