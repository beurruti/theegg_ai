#He aquí mi primer programa. Lo he hecho lo más sencillo posible aunque sé que puede haber muchas mejoras. Muchas gracias de antemano 
#Author: beurruti

try: 
        decimal = float(input("Introduce un número entre 0 y 0.9999 con un maximo de 4 digitos decimales (si marcas 1, sales del programa): "))
        numerador = int(float(decimal) * 10000)
        denominador = 10000
        i = numerador

        if decimal <= 0: 
            print ("Debes introducir un número mayor a 0. Vuelve a ejecutar el programa. Gracias.")
        elif decimal >1: 
            print ("Debes introducir un número menor a 1. Vuelve a ejecutar el programa. Gracias.")
        elif decimal==1: 
            print ("Final del programa")
        else: 
            while i > 1 :
                
                if numerador % i == 0 and denominador % i == 0:
                   numerador = numerador / i
                   denominador = denominador / i
                   print ("La Fracción mínima de %.4f es: %d/%d" %(decimal, numerador, denominador))    
                   print ("Si quieres realizar otra operación, vuelve a ejecutar el programa. Gracias.")
                i =  i - 1 
except: 
        print ("Solamente se admiten números, lo siento. Vuelve a intentarlo. Para los números por favor utiliza el punto y no la coma. Vuelve a ejecutar el programa. Gracias.")
    
















