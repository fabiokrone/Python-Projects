import geocoder
import folium

#retrieve your own IP address
g = geocoder.ip("me")

#myAddress gets latitude and longitude from your IP address
myAddress = g.latlng

my_map1 = folium.Map(location=myAddress,
                     zoom_start=12)

folium.CircleMarker(location=myAddress,
                    radius=50, popup="Sua Localização").add_to(my_map1)

folium.Marker(myAddress,
              popup="Sua Localização").add_to(my_map1)

#creates a html map
my_map1.save("my_map.html ")
