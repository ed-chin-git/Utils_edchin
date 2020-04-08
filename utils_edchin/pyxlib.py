# _______How to use this module_____________________________
#  import utils_edchin.pyxlib as pyx
import numpy as np


class pyxlib():
    def __init__(self):
        """
                # --- PREVIOUS VERSION ---
                # -- define class
                class = pyxlib(df1)
                    def __init__(self, my_df):
                        self.df = my_df.copy()
                        return
                    def another_function(self)
                        new_df = self.df.copy()
                        return

                # -- instantiate obj from class def
                pyx = pyxlib(df1) # class attrib holds passed-in df

        Input Params : none
        Sample call : pyx = DataProcessor()
                      df_out = processor.add_state_names(df_in)
        """

    def variance_edc(self, numbers):
        # ___ Variance:average of the squared differences from the mean____
        #  call : pyx.variance_edc([4,5,6,7])

        # ___ calculate mean________________
        me_an = sum(numbers) / len(numbers)

        # ____calculate variance using a list comprehension_______
        return sum((x - me_an) ** 2 for x in numbers) / len(numbers)

    def create_kaggle_submission(self, pred_array, x_test_df, dest_url):
        '''
        _____ Create a csv file for submission to Kaggle __________
          submission_url = '/content/drive/My Drive/submission.csv
          pyx.create_kaggle_submission(predictions,test_features,submission_url)
        '''
        pred_df = pandas.DataFrame(pred_array, columns=['status_group'])
        ids = pandas.DataFrame(x_test_df.id, columns=['id'])
        ids = ids.astype('int32')
        submit_df = pandas.concat([ids, pred_df], axis=1)
        submit_df.to_csv(dest_url, index=False, header=['id', 'status_group'])
        return

    def train_val_test_split(self, X, y, train_size=0.8, val_size=0.1,
                             test_size=0.1, random_state=None, shuffle=True):
        '''
            ___ Split model data into Train/Val/Test sets ___

        '''
        # Split sizes need to add up to 1.0
        assert train_size + val_size + test_size == 1
        #  1st split creates train & test
        X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state, shuffle=shuffle)
        # 2nd split train into train & val
        X_train, X_val, y_train, y_val = train_test_split(
            X_train_val, y_train_val, test_size=val_size/(train_size+val_size),
            random_state=random_state, shuffle=shuffle)
        return X_train, X_val, X_test, y_train, y_val, y_test

    def removeOutliers(self, input_list):
        # TODO need to assert that input_list
        # contains numeric items only
        input_array = np.array(input_list)
        upper_quartile = np.percentile(input_array, 75)
        lower_quartile = np.percentile(input_array, 25)
        IQR = (upper_quartile - lower_quartile) * 1.5
        quartileSet = (lower_quartile - IQR, upper_quartile + IQR)
        resultList = []
        for y in np.nditer(input_array):
            if y >= quartileSet[0] and y <= quartileSet[1]:
                resultList.append(y.item())  # .item() to avoid returning array
        return resultList

    def quartileSet(self, input_list):
        # TODO need to assert that input_list
        # contains numeric items only
        input_array = np.array(input_list)
        upper_quartile = np.percentile(input_array, 75)
        lower_quartile = np.percentile(input_array, 25)
        IQR = (upper_quartile - lower_quartile) * 1.5
        quartileSet = (lower_quartile - IQR, upper_quartile + IQR)
        return quartileSet

    def listOutliers(self, input_list):
        # TODO need to assert that input_list
        # contains numeric items only
        input_array = np.array(input_list)
        upper_quartile = np.percentile(input_array, 75)
        lower_quartile = np.percentile(input_array, 25)
        IQR = (upper_quartile - lower_quartile) * 1.5
        quartileSet = (lower_quartile - IQR, upper_quartile + IQR)
        resultList = []
        for y in np.nditer(input_array):
            if y <= quartileSet[0] or y >= quartileSet[1]:
                resultList.append(y.item())  # .item() to avoid returning array
        return resultList

    def str_reverse(self, in_str):
        return (in_str[::-1])

    def str_reverse2(self, in_str):
        return str_reverse(in_str)

#  To run / test this module locally
if __name__ == '__main__':
    # insert testing /calling code
    # call the function inside the print statement
    # to see results in terminal window

    pyx = pyxlib()  # instantiate object

    #  Call Functions
    print('\n')
    print('TURBO reversed string =',pyx.str_reverse('TURBO'),'\n')
    print('TURBO reversed string =',pyx.str_reverse('TURBO'),'\n')

    num_list = [-10, 2, 5, 3, 8, 4, 7, 5, 10, 99, 1000]
    print('List :', num_list)

    qSet = pyx.quartileSet(num_list)
    print('Quartile limit-Lower:', qSet[0])
    print('               Upper:',qSet[1])
    print('Outliers :',pyx.listOutliers(num_list))
    print('wo/Outliers :', pyx.removeOutliers(num_list))    
    print('        Var :', pyx.variance_edc(pyx.removeOutliers(num_list)))
