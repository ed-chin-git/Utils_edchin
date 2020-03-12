# ======================================================
#  Packaging Python Projects Tutorial : https://packaging.python.org/tutorials/packaging-projects/ 
#
#  Installation : #  pip install -i https://test.pypi.org/simple/ lambdata-edchin
#
#
# ===================================================================


#  Importing
import lambdata_edchin.pyxlib as pyx
dir(pyx)

#  Using create_kaggle_submission(pred_array,x_test_df,dest_url):
#  inputs : predictions array
#           X_test dataframe  
#           csv destination url  
#  outputs :  .csv file formatted for kaggle submission 