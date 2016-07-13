"""
run.py project file

"""
from imposm.parser import OSMParser

# simple class that handles the parsed OSM data.
class HighwayCounter(object):
    highways = 0

    def ways(self, ways):
        # callback method for ways
        for osmid, tags, refs in ways:
            if 'highway' in tags:
              self.highways += 1

# instantiate counter and parser and start parsing
counter = HighwayCounter()
p = OSMParser(concurrency=4, ways_callback=counter.ways)
p.parse('data/zachodniopomorskie-latest.osm.pbf')

# done
print counter.highways