from gcd_algorithm import gcd_algorithm

def test_gcd_algorithm():
    # ut to statue of liberty
    assert(2400 <= gcd_algorithm(6378.1, (30.285, -97.7335), (40.6892, -74.0445)) <= 2500)
    # ut to sydney opera house
    assert(13600 <= gcd_algorithm(6378.1, (30.285, -97.7335), (-33.8568, 151.2153)) <= 13700)
    #ut to machu picchu
    assert(5450 <= gcd_algorithm(6378.1, (30.285, -97.7335), (-13.1632, -72.5453)) <= 5550)
    #ut to taj mahal
    assert(13550 <= gcd_algorithm(6378.1, (30.285, -97.7335), (27.1751, 78.0421)) <= 13650)
