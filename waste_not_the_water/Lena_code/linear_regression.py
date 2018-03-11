import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import pandas.tseries
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.metrics import r2_score
import pickle

def data_cleaning():
    df_cap = pd.read_csv('T_UWWTPS.csv')
    df_cap2 = df_cap.drop(df_cap.index[4332]) # remove abnormal point
    df_temp = pd.read_csv('location_temperature.csv')
    df_cap3 = df_cap2[['uwwLatitude', 'uwwLongitude']]
    df_cleaned = pd.DataFrame(data = {'LoadEntering': df_cap2['uwwLoadEnteringUWWTP'],'Capacity': df_cap2['uwwCapacity'], 
                            'T': df_temp['temperature'],'NRemoval':df_cap2['uwwNRemoval'],'PRemoval':df_cap2['uwwPRemoval'],
                            'Longitude': df_cap3['uwwLongitude'], 'Latitude':df_cap3['uwwLatitude']})
    df_no_missing = df_cleaned.dropna()
    df_no_zeros = df_no_missing[df_no_missing.LoadEntering != 0]
    df = df_no_zeros[df_no_zeros.Capacity != 0]
    return df

# use this wrapped function for data training
# input data as a dataframe used for training
def linear_regression_result():
    df = data_cleaning()
    df_train, x_test, y_test = split_train_test(df)
    filename, y_predict = linear_regr(df_train, x_test)
    r_2 = r2_score(y_test, y_predict)
    return r_2, filename
    
def split_train_test(df):
    x = df[['LoadEntering', 'Longitude', 'Latitude']]
    y = df['Capacity']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
    df_train = pd.DataFrame(data = {'Capacity':y_train, 'LoadEntering':x_train['LoadEntering'], 
                                'Longitude':x_train['Longitude'], 'Latitude':x_train['Latitude']})
    return df_train, x_test, y_test

def linear_regr(df_train, x_test):
    model = smf.ols("Capacity ~ LoadEntering + Longitude * Latitude", df_train)
    result = model.fit()
    y_predict = result.predict(x_test)
    filename = "linear_result.sav"
    object_loc = open(filename, 'wb')
    pickle.dump(result, object_loc)
    object_loc.close()
    return filename, y_predict

# this function is used for interactive purpose
# input filename for the prediction. It should be shown after you call that wrapped function
def customer_inter(customer, filename):
    result = pickle.load(open(filename, 'rb'))
    y_customer = result.predict(customer[['Latitude', 'Longitude', 'LoadEntering']])
    return y_customer


