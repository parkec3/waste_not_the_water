import linear_regression as lr
import pandas as pd
import numpy as np

def test_split_train_test():
    df = pd.read_csv('clean.csv')
    df_sample = df.sample(100)
    df_train, x_test, y_test = lr.split_train_test(df_sample)
    if df_train.empty == True:
        raise Exception('DataFrame is broken!')
    if len(x_test) != 20:
        raise Exception('Wrong train_test_split function!')

def test_linear_regr():
    df = pd.read_csv('clean.csv')
    df_train = df.sample(80)
    x_test = df[['LoadEntering', 'Longitude', 'Latitude']].sample(20)
    result, y_predict = lr.linear_regr(df_train, x_test)
    
    assert np.isnan(y_predict).any() == False, 'Prediction function has an error!'
