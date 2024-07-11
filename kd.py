# %%

from scipy.spatial import KDTree
import numpy as np

def haversine_distance(coord1, coord2):
    R = 6371  # Radius of the Earth in kilometers
    lat1, lon1 = np.radians(coord1)
    lat2, lon2 = np.radians(coord2)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return R * c

def find_points_within_distance_kdtree(points, center_point, max_distance):
    kdtree = KDTree(points)
    indices = kdtree.query_ball_point(center_point, max_distance / 6371)  # Convert distance to radians
    nearby_points = [points[i] for i in indices if haversine_distance(points[i], center_point) <= max_distance]
    return nearby_points

# Example usage
points = np.array([(38.0337, -122.7967), (38.0152, -122.7959), (37.9927, -122.7914), (37.99723, -122.79805), (37.98922, -122.78795)])
center_point = (38.0, -122.8)
max_distance = 50  # kilometers

nearby_points = find_points_within_distance_kdtree(points, center_point, max_distance)
print(f"Points within {max_distance} km: {nearby_points}")

# %%
