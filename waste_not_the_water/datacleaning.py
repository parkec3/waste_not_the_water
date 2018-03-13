import pandas as pd
data = pd.read_csv('data/T_UWWTPS.csv')
df_toclean = pd.DataFrame(data = {'Member State': data['rptMStateKey'], 'Latitude': data['uwwLatitude'], 
'Longitude': data['uwwLongitude'], 'LoadEntering': data['uwwLoadEnteringUWWTP'], 'Capacity': 
data['uwwCapacity'], 'NRemoval': data['uwwNRemoval'], 'PRemoval': data['uwwPRemoval']})
df_no_missing = df_toclean.dropna()
