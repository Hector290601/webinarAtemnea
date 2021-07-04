#-*-coding:utf-8 -*-
palabra = input("Dame una palabra a cifrar: ")
cifra = int(input("Introduce la cifra de césar: "))
palabraEncriptada = ""
for letra in palabra:
    if letra.isupper():
        lA = ord(letra)
        lId = ord(letra) - ord('A')
        nId = (lId + cifra) % 26
        palabraEncriptada = palabraEncriptada + chr(nId + ord('A'))
    else:
        lA = ord(letra)
        lId = ord(letra) - ord('a')
        nId = (lId + cifra) % 26
        palabraEncriptada = palabraEncriptada + chr(nId + ord('a'))
print("Tu palabra es:  ", palabra, " y la palabra cifrada: ", palabraEncriptada)

