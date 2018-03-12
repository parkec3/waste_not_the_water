import numpy as np
import pandas as pd
import math

def NP_removal(df, customer):
    df_s = []
    df_nons = []
    for i in range(len(df)):
        if customer.iloc[0].NRemoval == df.iloc[i].NRemoval or customer.iloc[0].PRemoval == df.iloc[i].PRemoval:
            df_s.append(df.iloc[i])
        else:
            df_nons.append(df.iloc[i])
    nearest_s, r_s = nearest_point(pd.DataFrame(df_s).reset_index(drop=True), customer)
    nearest_nons, r_nons = nearest_point(pd.DataFrame(df_nons).reset_index(drop=True), customer)
    index = ['NP satisfied', 'NP not satisfied']
    df_NP = pd.DataFrame([nearest_s, nearest_nons], index=index)
    return df_NP

def nearest_point(df, customer):
    min_r = math.sqrt((customer.LoadEntering[0] - df.iloc[0].LoadEntering)**2 + (customer.Longitude[0] - df.iloc[0].Longitude)**2 + (customer.Latitude[0] - df.iloc[0].Latitude)**2)
    min_index = 0
    for i in range(1, len(df) - 1):
        r = math.sqrt((customer.LoadEntering[0] - df.iloc[i].LoadEntering)**2 + (customer.Longitude[0] - df.iloc[i].Longitude)**2 + (customer.Latitude[0] - df.iloc[i].Latitude)**2)
        if r < min_r:
            min_r = r
            min_index = i
    nearest = df.iloc[min_index]
    return nearest, r
