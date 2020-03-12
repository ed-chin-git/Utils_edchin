# _______How to use this module_____________________________
#  import lambdata_edchin.pyxlib as pyx

def variance_edc(numbers):
    # ___ Variance:average of the squared differences from the mean____
    #  call : pyx.variance_edc([4,5,6,7])

    #___ calculate mean________________
    me_an=sum(numbers) / len(numbers)

    #____calculate variance using a list comprehension__________
    return sum((x - me_an) ** 2 for x in numbers) / len(numbers)

#______ Create a csv file for submission to Kaggle _______________________
#   submission_url = '/content/drive/My Drive/submission.csv'
#   pyx.create_kaggle_submission(predictions,test_features,submission_url)

def create_kaggle_submission(pred_array,x_test_df,dest_url):
  pred_df=pandas.DataFrame(pred_array,columns=['status_group'])
  ids=pandas.DataFrame(x_test_df.id,columns=['id'])
  ids=ids.astype('int32')
  submit_df=pandas.concat([ids, pred_df], axis=1)
  submit_df.to_csv(dest_url, index=False, header=['id','status_group'])
  return

#______ Split model data into Train/Val/Test sets ___________
def train_val_test_split(X, y, train_size=0.8, val_size=0.1, test_size=0.1, 
                         random_state=None, shuffle=True):
     
    assert train_size + val_size + test_size == 1
    
    X_train_val, X_test, y_train_val, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, shuffle=shuffle)
    
    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val, y_train_val, test_size=val_size/(train_size+val_size), 
        random_state=random_state, shuffle=shuffle)
    
    return X_train, X_val, X_test, y_train, y_val, y_test

#  To run / test this module locally
if __name__ == '__main__':
    # insert testing /calling code
    # call the function inside the print statement 
    # to see results in terminal window
    print(variance_edc([5,25,99,1325,1125,555,6546,888]) )