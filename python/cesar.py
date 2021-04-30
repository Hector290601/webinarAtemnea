#-*-coding:utf-8 -*-
"""
    Comentarios
    largos
    y
    especiales
"""
#Comentarios cortos de una sola línea
"""
    A B C número de la letra
    D E F número de la letra más tres
    casteo:
        Cambia el tip de dato de una variable
    Se hace:
        nuevaVariable = nuevoTipoDeDato(VariableConAntigüo tipo de dato)
        nuevoTipoDeDato(VariableConAntigüo tipo de dato)
"""
palabra = input("Dame una palabra a cifrar: ")
cifra = int(input("Introduce la cifra de césar: "))
"""
    for variable in rango:
        cuerpoDeFor
"""
palabraEncriptada = ""
for letra in palabra:
    """
        if condicion:
            cuerpo
    """
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
