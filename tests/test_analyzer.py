from analyzer.text_analyzer import contar_palabras, contar_caracteres, contar_vocales, contar_lineas


def test_contar_palabras():
    assert contar_palabras("Hola mundo") == 2


def test_contar_caracteres():
    assert contar_caracteres("Hola") == 4


def test_contar_vocales():
    assert contar_vocales("Hola") == 2

def test_contar_lineas():
    assert contar_lineas("Hola\nMundo") == 2    