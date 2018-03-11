import pyowm
owm = pyowm.OWM('c0a3763a4ae7f31677879de49df9de49') #unique API key
data = pd.read_csv('clean.csv')
lat = []
lon = []
lat = data['Latitude'].tolist()
lon = data['Longitude'].tolist()
location = pd.DataFrame({'Latitude': lat, 'Longitude': lon})

temp = []
for index, row in location.iterrows():
    obs = owm.weather_at_coords(float(row['Latitude']),float(row['Longitude']))
    a = obs1.get_weather()
    a.get_temperature('celsius')
    temp.append(a.get_temperature('celsius')['temp'])

location['temperature'] = temp
location.to_csv('location_temperature.csv')
