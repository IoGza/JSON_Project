import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

infile = open("eq_data_1_day_m1.json", "r")
outfile = open("readable_ed_data.json", "w")

# converts data into a format Python
# can work with: in this case, a giant dictionary
eq_data = json.load(infile)


json.dump(eq_data, outfile, indent=4)

list_of_eqs = []

list_of_eqs = eq_data["features"]

# print(list_of_eqs)

mags, longs, latds = [], [], []
# eq is already the sub 0 index value, so only
# properties and mag need to be indexed to get each eq magnitude
for eq in list_of_eqs:
    mag = eq["properties"]["mag"]
    long = eq["geometry"]["coordinates"][0]
    latd = eq["geometry"]["coordinates"][1]

    mags.append(mag)

    longs.append(long)

    latds.append(latd)


print(mags[:10])
print(longs[:10])
print(latds[:10])



data = [Scattergeo(lon=longs, lat=latds)]

my_layout = Layout(title="Global Earthquakes")

fig = {'data':data,'layout':my_layout}

offline.plot(fig, filename="global_earth")