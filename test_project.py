import pytest
from project import Planet, YELLOW, BLUE, RED, DARK_GREY, WHITE

@pytest.fixture
def sun_earth_system():
    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10 ** 30)
    sun.sun = True

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10 ** 24)
    earth.y_vel = 29.783 * 1000

    return sun, earth


def test_distance_calculation(sun_earth_system):
    sun, earth = sun_earth_system
    sun.update_position([earth])
    earth.update_position([sun])

    distance_earth_to_sun = earth.distance_to_sun
    expected_distance = Planet.AU
    assert pytest.approx(distance_earth_to_sun, abs=1e-6) == expected_distance



def test_attraction_calculation(sun_earth_system):
    sun, earth = sun_earth_system
    force_x, force_y = earth.attraction(sun)

    assert force_x is not None
    assert force_y is not None
