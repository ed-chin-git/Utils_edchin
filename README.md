# Data Science Utilities in Python

## Python Package site :
   https://test.pypi.org/project/utils-edchin/

## Git Repo
   https://github.com/ed-chin-git/Utils_edchin

## Packaging Python Projects Tutorial
   https://packaging.python.org/tutorials/packaging-projects/ 

## Developer Workflow:
   Make & test code changes locally
   
   Pushcode changes to Github

   Update version=(new version number) in setup.py & utils_edchin/__init__.py

   Delete any existing distribution files in dist/ subdirectory

   Create distribution files : Saves a compressed version of the code in the dist/ subdirectory

      python setup.py sdist bdist_wheel    

   Upload the package to the test PyPI server, where it can be downloaded by others via pip commands    

      twine upload --repository-url https://test.pypi.org/legacy/ dist/* 
               

## Installation
                pip install -i https://test.pypi.org/simple/ utils-edchin

### Importing
                import utils_edchin.pyxlib as pyx
                dir(pyx)

###  Calling Functions
   ## create_kaggle_submission(pred_array,x_test_df,dest_url):

                                 inputs : predictions array
                                       X_test dataframe  
                                       csv destination url  
                                 outputs :  .csv file formatted for kaggle submission
