import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap
import pandas as pd
import folium
from pandas import *

def data_import_clean():
    """ This function does not accept any parameter"""
    """ It cleans and organizes raw csv data and returns resulting dataframe"""
    df= pd.read_csv('T_UWWTPS.csv')
    df_toclean = pd.DataFrame(data = {'aggID': df['aggID'],'Latitude': df['uwwLatitude'],'Longitude': 
                                       df['uwwLongitude'],'LoadEntering': df['uwwLoadEnteringUWWTP'],
                                       'Capacity': df['uwwCapacity']}) #Selecting interested columns 
					
    df_indexed = df_toclean.set_index('aggID')
    dff = df_indexed.dropna() #Drop NaN rows
    dff = dff.sort_values('Capacity') # Rerrange rows based on capacity in ascending order
    return dff

def create_basic_list(dff):
    """This function create lists from Capcity, Latitude,Longitude column of organized dataframe"""
    """ It returns four lists:latitude,longitude,capacity and magnitude which scales capacity 1000000 times down"""
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
    """The function takes parameter: capacity list and specific element of list"""
    """It returns a color assigned to that element"""
    #The list should arranged in ascenting order
    #We need to make sure that the index is an integer
    if index < list[int(len(list)/3)]:
        return('ro') # The fisrt 1/3 of elements would be red on map
    elif index < list[int(len(list)/3*2)]:
        return('go') # The second 1/3 of elements would be green on map
    else:
        return('yo') #The rest would be yellow on map

def get_color_graph(lons,lats,capacity):
    """The function takes as parameters: longitude list,latitude list and capacity list"""
    """It gives a map with points colored based on their capacity"""
    # set the basemap up 
    plt.figure(figsize=(15,12))
    plt.xlabel('longitude',fontsize=8)
    plt.ylabel('latitude',fontsize=8)
    
  
    #Here decides the basic properties of map such as resolution and boundary
    #The map type is Mercator. The coastlines or lake with an area smaller than 1000.0
    #in km^2 will not be plotted. The longitude and latitude of lower left are 10.0 and 40.0
    # The longitude and latitude of upper right are 30.0 and 70.0. The center is -130 and 0.
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
    """ The function takes as parameters: longitude list,latitude list and magnitude list"""
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
        msize = mag * min_marker_size # Here makes sure that the dots size are based on their capacity.
        base_map1.plot(x, y, 'ro', markersize=msize)

    plt.show()

def create_interactive_map(lat,lon,capacity):
    """The function takes as parameters:latitude list,longitude list and capacity list"""
    """It returns a map that could be zoom in and out with selective data points on """
    # Here the map is set up with center of (25,45)
    interactive_map = folium.Map(location=[25,45],zoom_start=5)
    for lat0, lon0, cap in zip(lat, lon, capacity):
        folium.Marker([lat0,lon0],popup="Capacity: "+str(cap)+" Latitude:"+str(lat0)+",Longitude: "+str(lon0)).add_to(interactive_map)
    return interactive_map

def interactive_customer_map(customer,i):
    """The function takes customer's DataFrame and the specific row index of Frame as parameters"""
    """It returns a map contains customer data point two points calculted from Nearest_N machine model """
    interactive_map = folium.Map(location=[25,45],zoom_start=3)# Setup the basic interactive model
    customer_new=customer.loc[[i]] #Make a single-row DataFrame of interested row of customer DataFrame
    result = nearest_n.NP_removal(customer_new)# Get a result DataFrame from Machine Learning Model
    lat_result = result['Latitude'].tolist() # Make lists from result to be ready for add points to map
    lon_result = result['Longitude'].tolist()
    Pop_string = ['CUSTOMER','NP_REMOVAL','NP_NONREMOVAL']
    NR = result['NRemoval'].tolist()
    NP = result['PRemoval'].tolist()
    for lat,lon,string,nr,np in zip(lat_result,lon_result,Pop_string,NR,NP):
        folium.Marker([lat,lon],popup=string+":"+" Latitude: "+str(lat)+",Longitude: "+str(lon)
                     +" ,NRemoval: "+str(nr)+" ,PRemoval: "+str(np),
                     icon=folium.Icon(color='red')).add_to(interactive_map)
        #The above map gives point with popup give information of result: latitude,longitude,whether it needs
        # Nitrogen or Phosphate removal
    return interactive_map
