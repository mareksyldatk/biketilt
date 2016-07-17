import matplotlib.pyplot as plt
import pandas
import tables
import numpy
from pylab import *


# Load data
roads = pandas.read_hdf("data/zachodniopomorskie.h5", key="roads")

# Plot
desired_road_types = ['motorway', 'motorway_link', 'trunk', 'primary', 'primary_link', 'secondary', 'tertiary', 'unclassified', 'road', 'residential']

clr = map(str, numpy.linspace(0.9, 0.1, len(desired_road_types)))
siz = numpy.linspace(2, .5, len(desired_road_types))

for ix, road_type in enumerate(reversed(desired_road_types)):
    plot_road = roads[roads['type'] == road_type]
    plt.scatter(plot_road['lon'], plot_road['lat'], c=clr[ix], s=siz[ix], edgecolors='none')

plt.title("Zachodniopomorskie")