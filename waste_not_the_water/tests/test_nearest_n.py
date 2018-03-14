import nearest_n
import numpy as np
import pandas as pd


def test_NP_removal():
    customer = pd.DataFrame(
        data={'LoadEntering': [6200.0],
              'Longitude': [17.0],
              'Latitude': [47.0],
              'NRemoval': [True],
              'PRemoval': [True]})
    df_NP = nearest_n.NP_removal(customer)
    if not isinstance(df_NP, pd.DataFrame):
        raise Exception('Bad type, not a DataFrame!')
    if df_NP.empty is True:
        raise Exception('Wrong append method!')


def test_nearest_point():
    df = pd.read_csv('clean.csv')
    df_sample = df.sample(100)
    customer = pd.DataFrame(
        data={'LoadEntering': [6200.0],
              'Longitude': [17.0],
              'Latitude': [47.0],
              'NRemoval': [True],
              'PRemoval': [True]})
    nearest = nearest_n.nearest_point(df_sample, customer)
    if nearest.empty is True:
        raise Exception('Function is broken!')
