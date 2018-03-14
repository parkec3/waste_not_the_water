import linear_regression as lr
import pandas as pd
import numpy as np
import os.path


def test_data_cleaning():
    df = lr.data_cleaning()
    if df.isnull().any().any() is True:
        raise Exception('Bad type, df is not a DataFrame!')
    if ((df.LoadEntering.all()) and (df.Capacity.all())) is False:
        raise Exception('Zeros in LoadEntering and Capacity!')


def test_linear_regression_result():
    df = pd.read_csv('clean.csv')
    df_sample = df.sample(100)
    r2_rr, filename_lr,
    r2_rr, mse_rr, filename_rr = lr.linear_regression_result()
    if r2_lr > 1 or r2_lr < 0 or r2_rr > 1 or r2_rr < 0:
        raise Exception('Coefficient function is wrong!')


def test_split_train_test():
    df = pd.read_csv('clean.csv')
    df_sample = df.sample(100)
    train, test = lr.split_train_test(df_sample)
    if (train.empty is True or test.empty is True):
        raise Exception('DataFrame is broken!')
    if (len(test) != 10 or len(train) != 90):
        raise Exception('Wrong train_test_split function!')


def test_linear_regr():
    df = pd.read_csv('clean.csv')
    df_train = df.sample(80)
    x_test = df[['LoadEntering', 'Longitude', 'Latitude']].sample(20)
    customer = pd.DataFrame(
        data={'LoadEntering': [6200.0],
              'Longitude': [17.0],
              'Latitude': [47.0]})
    filename, y_predict = lr.linear_regr(df_train, x_test)
    if y_predict.any() is float('Inf'):
        raise Exception('Prediction of customer cannot be infinite. \
            Linear Regression function is wrong!')
    assert np.isnan(y_predict).any() is False,
    'Prediction function has an error!'
    if os.path.isfile(filename) is False:
        raise Exception('File does not exist!')


def test_ridge_regr():
    df = pd.read_csv('clean.csv')
    train = df[['LoadEntering', 'Latitude',
                'Longitude', 'Capacity']].sample(80)
    test = df[['LoadEntering', 'Latitude',
               'Longitude', 'Capacity']].sample(20)
    filename, y_predict = lr.ridge_regr(train, test)
    if os.path.isfile(filename) is False:
        raise Exception('File does not exist!')


def test_customer_inter():
    customer = pd.DataFrame(
        data={'LoadEntering': [6200.0],
              'Longitude': [17.0],
              'Latitude': [47.0]})
    filename_lr = "linear_result.sav"
    filename_rr = "ridge_result.sav"
    y_customer_lr, y_customer_rr = lr.customer_inter(
        customer, filename_lr, filename_rr)
    if y_customer_lr.any() is float('Inf'):
        raise Exception('Prediction of customer cannot be infinite. \
            Linear Regression function is wrong!')
    if y_customer_rr.any() is float('Inf'):
        raise Exception('Prediction of customer cannot be infinite. \
            Ridge Regression function is wrong!')
