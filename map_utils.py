import osmnx as ox
def convert_lengths_to_floats(G):
    """
    Changes the attributes of the edges of graph G such that the 'length' field
    is a float rather than a string

    Parameters:
        G: the graph object

    Returns
        G: the graph object with updated lengths
    """
    for u, v, d in list(G.edges(data=True)):
        d['length'] = float(d['length'])

def get_data(city='Detroit', mode='bike'):
    '''
    Loads city transportation network data for a specified mode of transportation

    Parameters:
        city: The string of the city to use. Ex: Detroit, Amsterdam, Manhattan
        mode: The mode of transportation to import (bike, drive, pt, rail, walk)

    Returns:
        G: graph
    '''
    G = ox.load_graphml('{}_{}.graphml'.format(city, mode), folder='data/{}/'.format(city))
    convert_lengths_to_floats(G)
    return G
