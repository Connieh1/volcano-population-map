import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def elev_color(elev):
    if elev <= 1000:
        return "green"
    elif elev > 1000 and elev <= 2000:
        return "red"
    else:
        return "blue"


map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for lat, lon, elev in zip(lat, lon, elev):
    fg.add_child(folium.Marker(
        location=[lat, lon], popup="Elevation: "+str(elev)+"m", icon=folium.Icon(color=elev_color(elev))))
map.add_child(fg)
map.save("Map1.html")
