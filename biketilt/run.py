# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import pandas
import tables
import numpy
from pylab import *
import unicodedata
from trans import trans

from unidecode import unidecode

def transform(x):
    if x is not None:
       return trans(x)

def export_to_csv(data_frame, output_file):
    data_frame = data_frame.drop('order', 1)
    data_frame = data_frame.rename(columns={'lon': 'latitude', 'lat': 'longitude'})
    data_frame['name'] = data_frame['name'].apply(transform)
    data_frame[[u'id', u'name', u'latitude', u'longitude', u'point_id', u'type', ]].to_csv(output_file, encoding='utf-8')

# Load data
roads = pandas.read_hdf("data/pomorskie.h5", key="roads")

# Dump data to csv
# export_to_csv(roads, "csv/zachodniopomorskie.csv")

# Plot
# desired_road_types = ['motorway', 'motorway_link', 'trunk', 'primary', 'primary_link', 'secondary', 'tertiary', 'unclassified', 'road', 'residential']
#
# clr = map(str, numpy.linspace(0.9, 0.1, len(desired_road_types)))
# siz = numpy.linspace(2, .5, len(desired_road_types))
#
# for ix, road_type in enumerate(reversed(desired_road_types)):
#     plot_road = roads[roads['type'] == road_type]
#     plt.scatter(plot_road['lon'], plot_road['lat'], c=clr[ix], s=siz[ix], edgecolors='none')
#
# plt.title("Zachodniopomorskie")


def circle_radius(p1x, p1y, p2x, p2y, p3x, p3y):
    try:
        x1 = (p2x + p1x) / 2.
        y11 = (p2y + p1y) / 2.
        dy1 = p2x - p1x
        dx1 = -(p2y - p1y)

        x2 = (p3x + p2x) / 2.
        y2 = (p3y + p2y) / 2.
        dy2 = p3x - p2x
        dx2 = -(p3y - p2y)

        ox = (y11 * dx1 * dx2 + x2 * dx1 * dy2 - x1 * dy1 * dx2 - y2 * dx1 * dx2)/ (dx1 * dy2 - dy1 * dx2)
        oy = (ox - x1) * dy1 / dx1 + y11

        dx = ox - p1x
        dy = oy - p1y

        return np.sqrt(dx * dx + dy * dy)
    except:
        return None

def compute_radius(row):
    p1x, p1y = row['p_lat'], row['p_lon']
    p2x, p2y = row['lat'], row['lon']
    p3x, p3y = row['n_lat'], row['n_lon']

    if sum(isnan([ p1x, p1y, p2x, p2y, p3x, p3y ])) == 0:
        return circle_radius(p1x, p1y, p2x, p2y, p3x, p3y)
    else:
        return None


df = roads.sort_values(by=['id', 'order'])

df['p_lon'] = df.groupby(['id'])['lon'].shift(1)
df['p_lat'] = df.groupby(['id'])['lat'].shift(1)
df['n_lon'] = df.groupby(['id'])['lon'].shift(-1)
df['n_lat'] = df.groupby(['id'])['lat'].shift(-1)
df['radius'] = radius = df.apply(compute_radius, 1)
df = df.drop(['p_lat', 'p_lon', 'n_lat', 'n_lon'], 1)

df['mean_radius'] = df[['id','radius']].groupby(['id']).transform(mean)



# Plot
desired_road_types = ['motorway', 'motorway_link', 'trunk', 'primary', 'primary_link', 'secondary', 'tertiary', 'unclassified', 'road', 'residential']


data = df[df['type'].isin(desired_road_types)]
data = data[data['mean_radius'].notnull()]

data['mean_radius'] = np.log(data['mean_radius'])
data['mean_radius'] *= -1.
data['mean_radius'] = (data['mean_radius'] - data['mean_radius'].min()) / (data['mean_radius'].max() - data['mean_radius'].min())


fig, ax = plt.subplots()
data.plot(x='lon', y='lat', kind='scatter', c='mean_radius', cmap='hot', edgecolors='none', s=.001, ax=ax)
ax.set_axis_bgcolor('black')
plt.axis('equal')

fig.savefig('myimage.png', format='png', dpi=2400, bbox_inches='tight', pad_inches=0)



