'''
https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56

The presence of __init__.py file identifies the folder as a Python Package
And is used to mark which classes you want the user to access through the package interface.
  i.e  from Package.ClassFile import *

In this case:
     from utils_edchin.Dataprocessor import *


'''
VERSION='1.0.29'
import pandas
from sklearn.model_selection import train_test_split
from utils_edchin.DataProcessor import *
from utils_edchin.pyxlib import *
