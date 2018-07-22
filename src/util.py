import math

KM_PER_MILE = 1.60934
EARTH_RADIUS_KM = 6378.137

# The haversine formula:
# https://en.wikipedia.org/wiki/Haversine_formula
# http://www.movable-type.co.uk/scripts/latlong.html


def compute_lat_lng(lat_deg, lng_deg, bearing_deg, dist_mi):
	lat1 = math.radians(lat_deg)
	lng1 = math.radians(lng_deg)
	bearing = math.radians(bearing_deg)
	relative_dist = dist_mi * KM_PER_MILE / EARTH_RADIUS_KM
	lat2 = math.asin(math.sin(lat1) * math.cos(relative_dist) + math.cos(lat1) * math.sin(relative_dist) * math.cos(bearing))
	lng2 = lng1 + math.atan2(math.sin(bearing) * math.sin(relative_dist) * math.cos(lat1), math.cos(relative_dist) - math.sin(lat1) * math.sin(lat2))
	return (lat2, lng2)


def compute_dist_mi(lat1_deg, lng1_deg, lat2_deg, lng2_deg):
	delta_lat = math.radians(lat2_deg - lat1_deg)
	delta_lng = math.radians(lng2_deg - lng1_deg)
	lat1 = math.radians(lat1_deg)
	lat2 = math.radians(lat2_deg)

	a = math.sin(delta_lat/2) * math.sin(delta_lat/2) + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lng/2) * math.sin(delta_lng/2);
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a));

	return (EARTH_RADIUS_KM / KM_PER_MILE) * c;
	
