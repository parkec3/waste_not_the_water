import waste_not_the_water

import scipy
import numpy as np
import pandas as pd
from waste_not_the_water.linear_regression import data_cleaning
from scipy import spatial

def NP_removal(customer):
    df = data_cleaning()
    df_s = df[(df['NRemoval']==customer.iloc[0].NRemoval) & (df['PRemoval']==customer.iloc[0].PRemoval)]
    df_nons = df[(df['NRemoval']!=customer.iloc[0].NRemoval) | (df['PRemoval']!=customer.iloc[0].PRemoval)]
    nearest_s = nearest_point(df_s, customer)
    nearest_nons = nearest_point(df_nons, customer)
    index = ['customer', 'NP satisfied', 'NP not satisfied']
    df_NP = customer.append(nearest_s).append(nearest_nons)
    df_NP.index = ['customer', 'NP-Removal', 'NP-nonRemoval']
    return df_NP

def nearest_point(df, customer):
    c = customer.iloc[0].values.tolist()[0:3]
    df_sort = spatial.KDTree(df.iloc[:,1:4])
    index = df_sort.query(c)[1]
    nearest = df.iloc[index]
    return nearest
