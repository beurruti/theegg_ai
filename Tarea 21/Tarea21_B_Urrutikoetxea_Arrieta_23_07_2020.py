# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 08:10:14 2020

@author: Beñat Urrutikoetxea
"""
seguir="Si"
while seguir=="Si":
    try: 
        decimal = float(input("Introduce un número entre 0 y 0.9999 con un maximo de 4 digitos decimales (si marcas 1, sales del programa): "))
        numerador = int(float(decimal) * 100000)
        denominador = 100000
        i = numerador

        if decimal <= 0: 
            print ("Debes introducir un número mayor a 0. Gracias.")
        elif decimal >1: 
            print ("Debes introducir un número menor a 1. Gracias.")
        elif decimal==1: 
            print ("Final del programa")
            seguir="No"
        else: 
            while i > 1:
                
                if numerador % i == 0 and denominador % i == 0:
                   numerador = numerador / i
                   denominador = denominador / i
                   print ("La Fracción mínima de %.4f es: %d/%d" %(decimal, numerador, denominador))    
                   seguir=input("¿Quieres seguir metiendo números? (Si pulsas la palabra Si, seguirá preguntándote por un número: ")
                i =  i - 1 
    except: 
        print ("Solamente se admiten números, lo siento. Vuelve a intentarlo. Para los números por favor utiliza el punto y no la coma. Vuelve a ejecutar el programa. Gracias.")