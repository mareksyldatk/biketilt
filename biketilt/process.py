import pickle
import pandas
import os


def process_ways(ways, desired_way_types):
    # Filter and extract
    ways['type'] = ways.apply(lambda x: x['tags'].get('highway'), axis=1)
    ways['ref'] = ways.apply(lambda x: x['tags'].get('ref'), axis=1)
    ways['name'] = ways.apply(lambda x: x['tags'].get('name'), axis=1)
    ways = ways[ways['type'].isin(desired_way_types)].reset_index(drop=True)

    # unfold
    id_list = []
    order_list = []
    points_list = []
    type_list = []
    name_list = []

    for i in range(0, len(ways)):
        a_way = ways.iloc[[i]]
        way_points = list(a_way['refs'])[0]
        N = len(way_points)
        id_list += list(a_way['id']) * N
        order_list += range(0, N)
        points_list += way_points
        type_list += list(a_way['type'])*N
        name_list += list(a_way['name'])*N

    roads = pandas.DataFrame({'id': id_list,
                            'type': type_list,
                            'name': name_list,
                           'order': order_list,
                        'point_id': points_list})
    return roads


def join_ways_points(ways, points):
    points = points.rename(columns={'id': 'point_id'})
    roads = pandas.merge(ways, points, how='left', on=['point_id'])
    return roads


'''
Process file
'''
if __name__ == "__main__":

    # Load data
    FILENAMES = ['data/zachodniopomorskie.pickle', 'data/pomorskie.pickle']
    OUTPUT_FILE = ['data/zachodniopomorskie.h5', 'data/pomorskie.h5']

    for ix, FILE in enumerate(FILENAMES):
        with open(FILE, 'rb') as handle:
            [raw_ways, raw_points] = pickle.load(handle)

        # Process roads
        desired_way_types = ['motorway', 'motorway_link', 'trunk', 'primary', 'primary_link', 'secondary', 'tertiary', 'unclassified', 'road', 'residential']
        ways = process_ways(raw_ways, desired_way_types)
        roads = join_ways_points(ways, raw_points)

        # Dump roads
        FILENAME = OUTPUT_FILE[ix]
        if os.path.exists(FILENAME):
            os.remove(FILENAME)

        d = pandas.HDFStore(FILENAME, complevel=9, complib='blosc')
        d['roads'] = roads
        d.close()

