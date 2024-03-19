from bank import value

def test_value():
    assert value("hello") == 0
    assert value("Hello, Newman") == 0
    assert value("how you doing") == 20
    assert value("what's happening") == 100
    assert value("What's up!") == 100

