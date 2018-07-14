import folium

"""A program that uses Folium module to show a map coloured according to the population"""


map = folium.Map([20.2961, 85.8245], zoom_start=6, tiles="Mapbox Bright")


def color(x):
    if x['properties']['POP2005'] < 3000000:
        return 'green'
    elif x['properties']['POP2005'] < 5000000:
        return 'yellow'
    elif x['properties']['POP2005'] < 8000000:
        return 'orange'
    else:
        return 'red'


fg = folium.FeatureGroup(name="My Map")
fg1 = folium.FeatureGroup(name="My Station")
fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {"fillColor":color(x)}))
fg1.add_child(folium.GeoJson(data=open('stations.geojson', 'r', encoding='utf-8-sig').read()))
map.add_child(fg)
map.add_child(fg1)
map.add_child(folium.LayerControl())
map.save('map.html')

