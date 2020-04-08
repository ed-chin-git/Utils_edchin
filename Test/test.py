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
    import numpy as np
    import utils_edchin.pyxlib as edc_xlib  # import class
    pyx = edc_xlib()  # create instance

    num_list = [-10, 2, 5, 3, 8, 4, 7, 5, 10, 99, 1000]
    qSet = pyx.quartileSet(num_list)
    print('\nList :', num_list)
    print('Quartile limit-Lower:', qSet[0])
    print('               Upper:',qSet[1])
    print('    Outliers :', pyx.listOutliers(num_list))
    print('w/o Outliers :', pyx.removeOutliers(num_list))
    print('      my Var :', pyx.variance_edc(pyx.removeOutliers(num_list)))
    print('   Numpy.Var :', np.var(pyx.removeOutliers(num_list)))
    
    str_ing = 'Pennsylvania'
    print('\n', str_ing,'string reversed =', pyx.str_reverse(str_ing))
    
    import pandas 
    import utils_edchin.DataProcessor as edc_dp # import class
    dp = edc_dp()  # create instance
    df_in = pandas.DataFrame({"zip":[45763, 73627, 78632, 22374, 31455], "abbrev": ["OH", "MI", "SD", "PR", "PA"]})
    df_out = dp.add_state_names(df_in)  # use it
    print('\nInput:\n', df_in.head())
    print('Output:\n', df_out.head())
