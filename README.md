# Data Science Utilities in Python

## Python Package site :
   https://test.pypi.org/project/utils-edchin/

## Git Repo
   https://github.com/ed-chin-git/Utils_edchin

## Packaging Python Projects Tutorial
   https://packaging.python.org/tutorials/packaging-projects/ 
   
   https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56

## Developer Workflow:
   Make & test code changes locally
   
   Pushcode changes to Github

   Update version=(new version number) in setup.py & utils_edchin/__init__.py

   Delete any existing distribution files in dist/ subdirectory

   Create distribution files : Saves a compressed version of the code in the dist/ subdirectory

      python setup.py sdist bdist_wheel    

   Upload the package to the test PyPI server, where it can be downloaded by others via pip commands    

      twine upload --repository-url https://test.pypi.org/legacy/ dist/*   
        edchin  6feliciano9
               

## Installation
                pip install -i https://test.pypi.org/simple/ utils-edchin

### Importing
            import utils_edchin.pyxlib as edc
            edc = edc()
            edc.clear_terminal()

###  Calling Functions
   create_kaggle_submission(pred_array,x_test_df,dest_url):

         inputs : predictions array
                  X_test dataframe
                  csv destination url

         returns :  .csv file formatted for kaggle submission

   removeOutliers(input_list)

      based on : 
         upper_quartile = np.percentile(input_array, 75)
         lower_quartile = np.percentile(input_array, 25)
         IQR = (upper_quartile - lower_quartile) * 1.5
         quartileSet =
          (lower_quartile - IQR, upper_quartile + IQR)
         
         inputs : list of numbers

         returns : list of outliers