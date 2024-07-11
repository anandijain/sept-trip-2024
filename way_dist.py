# %%
import requests
import math

def fetch_osm_way(way_id):
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = f"""
    [out:json];
    way({way_id});
    (._;>;);
    out body;
    """
    response = requests.get(overpass_url, params={'data': overpass_query})
    data = response.json()
    return data

def calculate_distance(coord1, coord2):
    # Haversine formula to calculate distance between two coordinates in meters
    R = 6371000  # Radius of the Earth in meters
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    
    a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    return R * c

def get_way_length(way_id):
    data = fetch_osm_way(way_id)
    
    nodes = {node['id']: (node['lat'], node['lon']) for node in data['elements'] if node['type'] == 'node'}
    way = next(element for element in data['elements'] if element['type'] == 'way')
    
    way_nodes = way['nodes']
    print(way_nodes)
    length = 0.0
    for i in range(len(way_nodes) - 1):
        coord1 = nodes[way_nodes[i]]
        coord2 = nodes[way_nodes[i + 1]]
        length += calculate_distance(coord1, coord2)
    
    return length

way_id = 28917856
length = get_way_length(way_id)
print(f"The length of way {way_id} is {length:.2f} meters.")

# %%
ways = [
    28917912,
    28917815,
    28917838,
    28917781,
    28917722
]

l = list(map(get_way_length, ways))
# %%
l
# %%
d = sum(l)
# %%
d
# %%
# m to mi

d / 1609.34

# %%
