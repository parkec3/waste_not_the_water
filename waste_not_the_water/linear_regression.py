import waste_not_the_water

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import pandas.tseries
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.metrics import r2_score
import pickle
import xlrd
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error


def data_cleaning():
    df_cap = pd.read_csv('T_UWWTPS.csv')
    df_cap2 = df_cap.drop(df_cap.index[4332])  # remove abnormal point
    df_cleaned = pd.DataFrame(
        data={'LoadEntering': df_cap2['uwwLoadEnteringUWWTP'],
              'Capacity': df_cap2['uwwCapacity'],
              'NRemoval': df_cap2['uwwNRemoval'],
              'PRemoval': df_cap2['uwwPRemoval'],
              'Longitude': df_cap2['uwwLongitude'],
              'Latitude': df_cap2['uwwLatitude']})
    df_no_missing = df_cleaned.dropna()
    df_no_zeros = df_no_missing[df_no_missing.LoadEntering != 0]
    df = df_no_zeros[df_no_zeros.Capacity != 0]
    return df


# use this wrapped function for data training
# input data as a dataframe used for training
def linear_regression_result():
    df = data_cleaning()
    train, test = split_train_test(df)
    filename_lr, y_predict_lr = linear_regr(
        train, test[['LoadEntering', 'Longitude', 'Latitude']])
    r2_lr = r2_score(test.Capacity, y_predict_lr)
    filename_rr, y_predict_rr = ridge_regr(train, test)
    r2_rr = r2_score((test/test.std()).Capacity, y_predict_rr)
    mse_rr = mean_squared_error((test/test.std()).Capacity, y_predict_rr)
    return r2_lr, filename_lr, r2_rr, mse_rr, filename_rr


def split_train_test(df):
    df_split = df[['Capacity', 'LoadEntering', 'Longitude', 'Latitude']]
    train, test = train_test_split(
        df_split, test_size = 0.1, random_state = 1010)
    return train, test


def linear_regr(df_train, x_test):
    model = smf.ols("Capacity ~ LoadEntering + Longitude * Latitude", df_train)
    result = model.fit()
    y_predict = result.predict(x_test)
    filename = "linear_result.sav"
    object_loc = open(filename, 'wb')
    pickle.dump(result, object_loc)
    object_loc.close()
    return filename, y_predict


# Ridge Regression
def ridge_regr(train, test):
    train_normalized = train / train.std()
    test_normalized = test / test.std()
    heat_ridge = Ridge()
    a = 1e0
    heat_ridge.set_params(alpha = a)
    heat_ridge.fit(
        train_normalized[['Latitude', 'LoadEntering', 'Longitude']],
        train_normalized.Capacity)
    y_predict = heat_ridge.predict(
        test_normalized[['Latitude', 'LoadEntering', 'Longitude']])
    filename = "ridge_result.sav"
    object_loc = open(filename, 'wb')
    pickle.dump(heat_ridge, object_loc)
    object_loc.close()
    return filename, y_predict


# this function is used for interactive purpose
# input filename for the prediction.
# It should be shown after you call that wrapped function
def customer_inter(customer, filename_lr, filename_rr):
    result = pickle.load(open(filename_lr, 'rb'))
    heat_ridge = pickle.load(open(filename_rr, 'rb'))
    y_customer_lr = result.predict(
        customer[['Latitude', 'Longitude', 'LoadEntering']])
    y_customer_rr = heat_ridge.predict(
        customer[['Latitude', 'LoadEntering', 'Longitude']])
    return y_customer_lr, y_customer_rr
