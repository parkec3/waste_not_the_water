import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap
import pandas as pd
from pandas import *
import folium

import basemap

def test_data_import():
    dff =basemap.data_import_clean()
    dff.reset_index(inplace=True)
    c = dff['Capacity']
    for i in range(len(dff)-1):
        assert c[i] <= c[i+1],"The dataframe did not sort as expected"

def test_create_basic_list():
    dff = basemap.data_import_clean()
    lat,lon,capacity,magnitude = basemap.create_basic_list(dff)
    assert len(lat) == len(lon) == len(capacity) == len(magnitude),"List creation is not proper"

def test_color_marker():
    test_list = [4,9,44,64,78,90]
    color_list=[]
    for index in test_list:
        color = basemap.get_color_marker(test_list,index)
        color_list.append(color)
    
    assert color_list[0] == color_list[1],"Color distribution did not work as expected"
    assert color_list[3] == 'go',"Indexing is not proper"
