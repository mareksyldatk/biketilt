from imposm.parser import OSMParser
import pandas
import pickle

# Simple class that handles the parsed OSM data.
class Callbacks(object):
    coords = list()
    ways = list()

    def ways_callback(self, ways):
        # callback method for ways
        for osmid, tags, refs in ways:
            if 'highway' in tags:
                if 'trunk' in tags.values():
                    self.ways.append((osmid, refs))

    def coords_callback(self, coords):
        for osmid, lon, lat in coords:
            self.coords.append((osmid, lon, lat))


# Instantiate parser and start parsing
callbacks = Callbacks()

p1 = OSMParser(concurrency=4, coords_callback=callbacks.coords_callback)
p1.parse('data/zachodniopomorskie-latest.osm.pbf')

p2 = OSMParser(concurrency=4, ways_callback=callbacks.ways_callback)
p2.parse('data/zachodniopomorskie-latest.osm.pbf')

# Extracted data
data_coords = pandas.DataFrame(callbacks.coords)
data_coords.columns = ['id', 'lon', 'lat']

data_ways = pandas.DataFrame(callbacks.ways)
data_ways.columns = ['id', 'refs']

# Dump data
with open('extracted/zachodniopomorskie_trunk.pickle', 'wb') as handle:
    pickle.dump([data_ways, data_coords], handle)
