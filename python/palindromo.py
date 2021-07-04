#-*-coding:utf-8 -*-
palabra = input("Ingresa una palabra o frase: ")
palabraCadena = []

for caracter in palabra:
    if caracter != ' ':
        palabraCadena.append(caracter.lower())

if palabraCadena == palabraCadena[::-1]:
    print("Es un palíndromo :)")
else:
    print("No es un palíndromo :(")

print(palabra, palabraCadena)
