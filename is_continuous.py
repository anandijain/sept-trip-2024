# %% 
import requests

def fetch_osm_way(way_id):
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = f"""
    [out:json];
    way({way_id});
    out body;
    """
    response = requests.get(overpass_url, params={'data': overpass_query})
    data = response.json()
    return data

def get_way_nodes(way_id):
    data = fetch_osm_way(way_id)
    way = next(element for element in data['elements'] if element['type'] == 'way')
    return way['nodes']

def check_contiguity(ways):
    previous_end_node = None
    for way_id in ways:
        nodes = get_way_nodes(way_id)
        start_node = nodes[0]
        end_node = nodes[-1]
        
        if previous_end_node is not None and previous_end_node != start_node:
            return False
        
        previous_end_node = end_node
    
    return True

# List of way IDs
ways = [
    28917912,
    28917815,
    28917838,
    28917781,
    28917722
]

is_contiguous = check_contiguity(ways)
print(f"The list of ways is contiguous: {is_contiguous}")

# %%
# another thing is maybe just concat all the way nodes because 
#  likely the first node of the next way is NOT the last node of the previous way