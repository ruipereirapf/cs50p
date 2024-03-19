import pytest
from project2 import check_need_weather,get_latitude_longitude, check_prompt, City

def test_check_need_weather():
    assert check_need_weather("Yes") == True
    assert check_need_weather("yes") == True
    assert check_need_weather("Y") == True
    assert check_need_weather("y") == True
    assert check_need_weather("No") == False
    assert check_need_weather("no") == False
    assert check_need_weather("N") == False
    assert check_need_weather("n") == False

def test_get_latitude_longitude():
    assert get_latitude_longitude("41.72240, -8.12976") == ("41.72240","-8.12976")
    with pytest.raises(ValueError):
        get_latitude_longitude("N 41 22.671 W 7 51.588")

def test_check_prompt():

    # Mocking City instances for testing
    city1 = City(id=1,name="City1")
    city2 = City(id=2,name="City2")

    assert check_prompt("1",City) == "1"
    assert check_prompt("2",City) == "2"
