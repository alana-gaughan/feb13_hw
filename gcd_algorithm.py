import logging
from math import cos, sin, acos, radians


def gcd_algorithm(radius, geo_location_1, geo_location_2):
    """
    This function computes the great circle distance algorithm which finds the shortest distance between two points on the surface of a spehere.

    Args:
        radius (float): The radius of the sphere in the preferred units
        geo_location_1 (tuple): This tuple contains the latitude and longitude of the first location in decimal notation.
        geo_location_2 (tuple): This tuple contains the latitude and longitude of the second location in decimal notation.

    Returns:
        distance (float): The shortest distance between the two points
    """
    try:
        lat1 = radians(float(geo_location_1[0]))
        lat2 = radians(float(geo_location_2[0]))
        lon1 = radians(float(geo_location_1[1]))
        lon2 = radians(float(geo_location_2[1]))
    except ValueError:
        logging.warning("could not convert string to float: ''")

    distance = radius * acos(cos(lat1) * cos(lat2) * cos(lon1 - lon2) + sin(lat1) * sin(lat2))

    return distance
