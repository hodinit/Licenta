import folium
from geopy.geocoders import Nominatim


loc = Nominatim(user_agent="Geopy Library")
getLoc = loc.geocode("Cismigiu, Romania")

lat_cluj= 46.772166
long_cluj= 23.583807
lat_coruia= 47.56480680803573 # cordonate
long_coruia=23.60368731749156 #acasa

# uite alt comentariu

lat=getLoc.latitude
long=getLoc.longitude
map_start_point = folium.Map(location=[lat_cluj, long_cluj], zoom_start=13)
folium.Marker([lat_cluj,long_cluj ], popup="Parcare Opera Maghiara").add_to(map_start_point)

# entering the location name


# Add a marker
# folium.Marker([37.7749, -122.4194], popup="San Francisco").add_to(map_start_point)
# folium.Marker([46.556807, 23.808596], popup="Cluj").add_to(map_start_point)
# folium.Marker([47.56480680803573, 23.60368731749156], popup="Cosmin").add_to(map_start_point)
#folium.Marker([ 44.4361414 , 26.1027202], popup="Capitala").add_to(map_start_point)




# Save to an HTML file or display in a Jupyter Notebook
map_start_point.save("map.html")
print("Map saved as map.html!")



# calling the Nominatim tool and create Nominatim class




# printing address
print(getLoc.address)

# printing latitude and longitude
print("Latitude = ", getLoc.latitude, "\n")
print("Longitude = ", getLoc.longitude)