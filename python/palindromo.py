#-*-coding:utf-8 -*-
"""
    Comentarios
    largos
    y
    especiales
"""
#Comentarios cortos de una sola línea
palabra = input("Ingresa una palabra o frase: ")
"""
    palabraCadena = [] + [cacter]
    palabraCadena = [cacter] + [cacter]
    palabraCadena = [cacter, cacter]
"""
palabraCadena = []

for caracter in palabra:
    if caracter != ' ':
        palabraCadena.append(caracter.lower())

if palabraCadena == palabraCadena[::-1]:
    print("Es un palíndromo :)")
else:
    print("No es un palíndromo :(")

print(palabra, palabraCadena)
