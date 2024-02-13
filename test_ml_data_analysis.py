from ml_data_analysis import percent_per_year, standard_dev, find_closest

def test_percent_per_year():
    assert percent_per_year([{'year': 2001, "fall": "Found"}, {'year': 1998, "fall":"Fell"}], 'fall', 'year', "Found") == {1998: 0, 2001: 100}
    assert percent_per_year([ {'a':2000, 'b':'c'},
        {'a': 2024, 'b':'c'},
        {'a': 2000, 'b':'d'}], 
        'b', 'a', 'c') == {2000: 50, 2024: 100}
    assert percent_per_year([{'a': 1990, 'b':'c'}, {'a':1991, 'b':'d'}, {'a':1990, 'b':'c'}, {'a':1992, 'b':'c'}, {'a':1992, 'b':'d'}], 'b', 'a', 'c') == {1990 : 100, 1991:0, 1992:50}
    return

def test_standard_dev():
    assert standard_dev( [{"a": 2}, {'a':3}, {'a':6}, {'a': 6}, {'a': 8}], "a")[1] == pytest.approx(2.449, .001)
    assert standard_dev( [{"a": 2}, {'a':3}, {'a':6}, {'a': 6}, {'a': 8}], "a")[0] == pytest.approx(5, .001)
    return

def test_find_closest():
    assert find_closest([{'name':'NYC','a':'(40.6892, -74.0445)'}, {'name':'Sydney Opera House', 'a':'(-33.8568, 151.2153)'}, {'name':'Machu Picchu','a':'(-13.1632, -72.5453)'}, {'name':'Taj Mahal','a':'(27.1751, 78.0421)'}], 'a', (30.285, -97.7335)) == [{'name':'NYC','a':'(40.6892, -74.0445)'}, {'name':'Machu Picchu','a':'(-13.1632, -72.5453)'}, {'name':'Taj Mahal','a':'(27.1751, 78.0421)'}, {'name':'Sydney Opera House', 'a':'(-33.8568, 151.2153)'}]
