import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import pandas.tseries
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.metrics import r2_score

def linear_regression_result(df, customer):
    df_train, x_test, y_test = split_train_test(df)
    result, y_predict, y_customer = linear_regr(df_train, x_test, customer)
    r_2 = r2_score(y_test, y_predict)
    return r_2, y_customer
    
def split_train_test(df):
    x = df[['LoadEntering', 'Longitude', 'Latitude']]
    y = df['Capacity']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
    df_train = pd.DataFrame(data = {'Capacity':y_train, 'LoadEntering':x_train['LoadEntering'], 
                                'Longitude':x_train['Longitude'], 'Latitude':x_train['Latitude']})
    return df_train, x_test, y_test

def linear_regr(df_train, x_test, customer):
    model = smf.ols("Capacity ~ LoadEntering + Longitude * Latitude", df_train)
    result = model.fit()
    y_predict = result.predict(x_test)
    y_customer = result.predict(customer[['Latitude', 'Longitude', 'LoadEntering']])
    return result, y_predict, y_customer
