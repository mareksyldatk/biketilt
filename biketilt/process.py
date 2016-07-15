import pandas
import pickle
import matplotlib.pyplot as plt


# Load data
with open('extracted/zachodniopomorskie_trunk.pickle', 'rb') as handle:
    [ways, points] = pickle.load(handle)

for i in range(0, 100):
    a_way = ways.iloc[[i]]
    way_points = list(a_way['refs'])[0]
    way_coords = points.loc[points['id'].isin(way_points)]
    way_lat = list(way_coords['lat'])
    way_lon = list(way_coords['lon'])

    plt.plot(way_lat, way_lon, '.')

    # print (way_lon[0], way_lat[0])
    # print (way_lon[-1], way_lat[-1])

plt.axis('equal')