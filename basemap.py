import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap
import pandas as pd
import folium
from pandas import *

def data_import_clean():
    df= pd.read_csv('T_UWWTPS.csv')
    df_toclean = pd.DataFrame(data = {'aggID': df['aggID'],'Latitude': df['uwwLatitude'],'Longitude': 
                                       df['uwwLongitude'],'LoadEntering': df['uwwLoadEnteringUWWTP'],
                                       'Capacity': df['uwwCapacity']}) #Selecting interested columns 
					
    df_indexed = df_toclean.set_index('aggID')
    dff = df_indexed.dropna() #Drop NaN rows
    dff = dff.sort_values('Capacity') # Rerrange rows based on capacity in ascending order
    return dff

def create_basic_list(dff):
    lats,lons=[],[]
    capacity = []
    magnitudes = []
    lats = dff['Latitude'].tolist()
    lons = dff['Longitude'].tolist()
    capacity = dff['Capacity'].tolist()
    for i in capacity:
        magnitudes.append(i/1000000) #Scale the capacity down for markersize on map
    return lats,lons,capacity,magnitudes

def get_color_marker(list,index):
    if index < list[int(len(list)/3)]:
        return('ro')
    elif index < list[int(len(list)/3*2)]:
        return('go')
    else:
        return('yo')

def get_color_graph(lons,lats,capacity):
    # set the basemap up 
    plt.figure(figsize=(15,12))
    plt.xlabel('longitude',fontsize=8)
    plt.ylabel('latitude',fontsize=8)
    
  
    #Here decides the basic properties of map such as resolution and boundary
    base_map = Basemap(projection='merc', resolution = 'l', area_thresh = 1000.0,
                       lat_0=0, lon_0=-130,llcrnrlat=40.0,llcrnrlon=-10.0,urcrnrlat=70.0,urcrnrlon=30.0)
    base_map.drawcoastlines()
    base_map.drawcountries()
    base_map.fillcontinents(color = 'gray')
    base_map.drawmapboundary()
    base_map.drawmeridians(np.arange(0, 360, 5),labels=[False,True,True,False])
    base_map.drawparallels(np.arange(-90, 90, 5),labels=[False,True,True,False])



    for lon, lat, cap in zip(lons, lats, capacity):
    	x,y = base_map(lon, lat)
   
    	base_map.plot(x, y, get_color_marker(capacity,cap), markersize=8)
 

    plt.show()
        
def get_size_map(lons,lats,magnitudes):
    plt.figure(figsize=(15,12))
    plt.xlabel('longitude',fontsize=10)
    plt.ylabel('latitude',fontsize=10)
    base_map1 = Basemap(projection='merc', resolution = 'l', area_thresh = 1000.0,
                        lat_0=0, lon_0=-130,llcrnrlat=40.0,llcrnrlon=-10.0,urcrnrlat=70.0,urcrnrlon=30.0)
    base_map1.drawcoastlines()
    base_map1.drawcountries()
    base_map1.fillcontinents(color = 'gray')
    base_map1.drawmapboundary()
    base_map1.drawmeridians(np.arange(0, 360, 5),labels=[False,True,True,False])
    base_map1.drawparallels(np.arange(-90, 90, 30),labels=[False,True,True,False])

    min_marker_size = 2.5                
    for lon, lat, mag in zip(lons, lats, magnitudes):
        x,y = base_map1(lon, lat)
        msize = mag * min_marker_size
        base_map1.plot(x, y, 'ro', markersize=msize)

    plt.show()

def create_interactive_map(lat,lon,capacity):
    interactive_map = folium.Map(location=[15,60],zoom_start=5)
    for lat0, lon0, cap in zip(lat, lon, capacity):
        folium.Marker([lat0,lon0],popup=str(cap)).add_to(interactive_map)
    return interactive_map
