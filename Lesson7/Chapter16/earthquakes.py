import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'Lesson7\Chapter16\data\earthquakes.json'
with open(filename) as f:
    allEqData = json.load(f)

readableFile = 'Lesson7\Chapter16\data\earthquakes.json'
with open(readableFile, 'w') as f:
    json.dump(allEqData, f, indent=4)

allEqDicts = allEqData['features']

mags, lons, lats, hoverTexts = [], [], [], []
for eqDict in allEqDicts:
    mag = eqDict['properties']['mag']
    lon = eqDict['geometry']['coordinates'][0]
    lat = eqDict['geometry']['coordinates'][1]
    title = eqDict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hoverTexts.append(title)
print(mags[:10])
print(lons[:5])
print(lats[:5])

# Map
data = [{
    'type' : 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'text' : hoverTexts,
    'marker' : {
        'size' : [5*mag for mag in mags],
        'color' : mags,
        'colorscale' : 'Viridis',
        'colorbar' : {'title' : 'Magnitude'},
    },
}]
myLayout = Layout(title = 'Global Earthquakes for March 2021')

fig = {'data' : data, 'layout' : myLayout}
offline.plot(fig, filename = 'global_earthquakes.html')