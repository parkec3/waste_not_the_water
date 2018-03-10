import nearest_n
import numpy as np
import pandas as pd

def test_NP_removal():
    df = pd.read_csv('clean.csv')
    df_sample = df.sample(100)
    customer = pd.DataFrame(data = {'LoadEntering': [6200.0], 'Longitude': [17.0], 'Latitude': [47.0], 'NRemoval': [True], 'PRemoval':[True]})
    df_NP = nearest_n.NP_removal(df_sample, customer)
    if not isinstance(df_NP, pd.DataFrame):
        raise Exception('Bad type, not a DataFrame!')
    if df_NP.empty == True:
        raise Exception('Wrong append method!')

def test_nearest_point():
    df = pd.read_csv('clean.csv')
    df_sample = df.sample(100)
    customer = pd.DataFrame(data = {'LoadEntering': [6200.0], 'Longitude': [17.0], 'Latitude': [47.0], 'NRemoval': [True], 'PRemoval':[True]})
    nearest_loc, r = nearest_n.nearest_point(df_sample, customer)
    if nearest_loc.empty == True:
        raise Exception('Function is broken!')
    if r == float('Inf'):
        raise Exception('Radius cannot be infinite number!')
