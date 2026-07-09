from app.conversor import celsius_para_fahrenheit, fahrenheit_para_celsius


def test_celsius_para_fahrenheit():
    assert celsius_para_fahrenheit(0) == 32
    assert celsius_para_fahrenheit(100) == 212


def test_fahrenheit_para_celsius():
    assert fahrenheit_para_celsius(32) == 0


def test_kelvin_para_celsius():
    from app.conversor import kelvin_para_celsius

    assert kelvin_para_celsius(273.15) == 0
