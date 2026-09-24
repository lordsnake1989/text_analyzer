from analyzer.text_analyzer import contar_palabras, contar_caracteres, contar_vocales


texto = input("Escribe un texto: ")

print("Palabras:", contar_palabras(texto))
print("Caracteres:", contar_caracteres(texto))
print("Vocales:", contar_vocales(texto))