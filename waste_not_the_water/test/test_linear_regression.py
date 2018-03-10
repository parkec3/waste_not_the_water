import linear_regression as lr
import pandas as pd
import numpy as np

def test_linear_regression_result():
    df = pd.read_csv('clean.csv')
    df_sample = df.sample(100)
    customer = customer = pd.DataFrame(data = {'LoadEntering': [6200.0], 'Longitude': [17.0], 'Latitude': [47.0]})
    r_2, y_customer = lr.linear_regression_result(df_sample, customer)
    if r_2 > 1 or r_2 < 0:
        raise Exception('Coefficient function is wrong!')
    if y_customer.any() == float('Inf'):
        raise Exception('Prediction of customer cannot be infinite. Linear Regression function is wrong!')

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
    customer = pd.DataFrame(data = {'LoadEntering': [6200.0], 'Longitude': [17.0], 'Latitude': [47.0]})
    result, y_predict, y_customer = lr.linear_regr(df_train, x_test, customer)
    if y_customer.any() == float('Inf'):
        raise Exception('Prediction of customer cannot be infinite. Linear Regression function is wrong!')
    assert np.isnan(y_predict).any() == False, 'Prediction function has an error!'
