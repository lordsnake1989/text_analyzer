def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)


def contar_caracteres(texto):
    return len(texto)


def contar_vocales(texto):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    return sum(1 for letra in texto if letra in vocales)