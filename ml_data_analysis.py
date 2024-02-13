import csv
import matplotlib.pyplot as plt
import logging
import gcd_algorithm
from math import sqrt

def percent_per_year(a_list_of_dicts, key_string1, year_key, string2):
    """
    This function counts the percent of meteorites per year that were detected match a characteristic.
    It can be used to count 'fall' vs 'fell' or to count the occurance of a specific class.

    Args:
        a_list_of_dicts (list): A list of dicts with the same keys
        key_string1 (string): key in each of the dicts that is associated with the desired category
        year_key (string): key to find the year stat
        string2 (string): the occurance of this string as the value to key_string1 is counted for each year

    Returns:
        percent_dict (dict): This dict contains the year as the key and the percentage of occurances of string2 as the value
    """
    count_dict = {}
    total_dict = {}
    percent_dict = {}

    for ml_dict in a_list_of_dicts:
        try:
            year = int(ml_dict[year_key])
            if year in total_dict.keys():
                total_dict[year] += 1
            else:
                total_dict[year] = 1
                count_dict[year] = 0
            if ml_dict[key_string1] == string2:
                count_dict[year] += 1
        except ValueError:
            logging.warning("Value Error: empty data entry")

    for year in sorted(total_dict.keys()):
        percent_dict[year] = (count_dict[year] / total_dict[year]) * 100

    return percent_dict


def standard_dev(a_list_of_dicts, key_string):
    """
    This function finds the standard deviation of the mass of the meteorites.

    Args:
        a_list_of_dicts (list): Data from the various meteorites
        key_string (string): this is the key to find the mass
        avg_mass (float): this is the average mass of the meteorite landings

    Returns:
        avg_mass (float): the average mass
        stdev (float): the standard deviation of the masses.
    """
    avg_mass = 0
    mass_count = 0
    for ml_dict in a_list_of_dicts:
        try:
            avg_mass += float(ml_dict[key_string])
            mass_count += 1
        except ValueError:
            logging.warning(f'encountered non-float value {ml_dict[key_string]} in standard_dev')
    avg_mass = avg_mass / mass_count

    stdev = 0
    for ml_dict in a_list_of_dicts:
        try:
            stdev += (float(ml_dict[key_string]) - avg_mass) ** 2
        except ValueError:
            logging.warning(f'encountered non-float value {ml_dict[key_string]} in standard_dev')
    stdev /= (mass_count - 1)
    stdev = sqrt(stdev)
    return avg_mass, stdev


def find_closest(a_list_of_dicts, key_string, location_tuple):
    """
    This function finds uses the gcd algorithm to find the closest 5 landing sites to a specified location.

    Args:
    a_list_of_dicts (list): Data from various meteorite landings where all dicts have the same keys.
    key_string (string): key to find the desired value
    location_tuple (tuple): Latitude and longitude of specified location in decimal form.

    Returns:
    closest_landings (list): list of 5 dictionaries of the closest landings with the gcd added as a key.
    """
    RADIUS = 6378.1
    closest_landings = []

    for ml_dict in a_list_of_dicts:
        try:
            location_str = ml_dict[key_string].strip("()")
            location_list = location_str.split(", ")
            if location_list[0] != '':
                gcd_km = gcd_algorithm.gcd_algorithm(RADIUS, location_tuple, tuple(location_list))
                ml_dict['gcd_km'] = gcd_km
                closest_landings.append(ml_dict)
        except ValueError:
            logging.warning(f'encountered non-tuple value {ml_dict[key_string]} in find_closest')

    closest_landings = sorted(closest_landings, key=lambda item: item["gcd_km"])

    return closest_landings


def main():
    logging.basicConfig(level='ERROR')
    
    ml_data = {'meteorite_landings': []}

    with open('Meteorite_Landings.csv', 'r', encoding="utf8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ml_data['meteorite_landings'].append(dict(row))

    avg_mass, stdev_mass = standard_dev(ml_data['meteorite_landings'], "mass (g)")

    print(f"Summary of Statistics:\nThe average mass is {avg_mass: .2f} kg with a standard deviation of +-{stdev_mass: .2f}.")

    closest_landings = find_closest(ml_data['meteorite_landings'], 'GeoLocation', (30.2850, -97.7335))

    print("\nFive meteorite landings closest to UT Austin:")
    i = 1
    for landing in closest_landings[:5]:
        print(f"{i}. {landing['name']: <20}\t({landing['gcd_km']:.2f} km away)")
        i += 1
    print("\nFive meteorite landings farthest from UT Austin:")
    i = 1
    for landing in closest_landings[:-6:-1]:
        print(f"{i}. {landing['name']: <20}\t({landing['gcd_km']:.2f} km away)")
        i += 1

    found_dict = percent_per_year(ml_data['meteorite_landings'], "fall", "year", "Found")
    plt.plot(found_dict.keys(), found_dict.values(), 'bo')
    plt.title("Percentage of 'Found' meteorites per year")
    plt.ylabel("percentage")
    plt.xlabel("year")
    plt.show()
    return


if __name__ == '__main__':
    main()
