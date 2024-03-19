from numb3rs import validate

def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.1000") == False
    assert validate("10.555.0.0") == False

def test_validate_bigger255():
    assert validate("512.512.512.512") == False

def test_validate_alpha():
    assert validate("cat") == False
    assert validate ("cat.cat.cat.cat") == False

def test_validate_dot():
    assert validate("255.255.255.255") == True
    assert validate("255a225a255a255") == False