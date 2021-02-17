import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def elev_color(elev):
    if elev <= 1500:
        return "green"
    elif elev > 1500 and elev <= 3000:
        return "red"
    else:
        return "blue"


map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

for lat, lon, elev in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(
        location=[lat, lon], radius=6, popup="Elevation: "+str(elev)+"m", fill_color=elev_color(elev), color='white', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                                                       else 'orange' if 10000000 < x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
