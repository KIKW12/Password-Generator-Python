'''Random se utiliza para generar aleatoriamente caracteres de la contraseña.'''
import random

'''
String proporciona constantes con caracteres como letras mayusculas y 
minusculas,digitos y caracteres especiales.
'''
import string

"""
================== Funcion para generacion de contraseña  =====================
"""

def generar_contraseña(longitud, usar_mayusculas, usar_especiales, 
                       usar_numeros, usar_primos):
    '''
    La funcion generar_contraseña
    recibe: longitud de la constraseña, usar_mayusculas un booleano que indica 
    si el usuario necesita o no letras mayusculas, usar_especiales un booleano
    que indica si se deben usar caracteres especiales, 
    usar_numeros un booleano que indica si se deben usar numeros en la 
    contraseña y usar_primos un booleano que indica si se deben de utilizar 
    numeros primos en la constraseña.
    regresa: una contraseña cumpliendo con las especificaciones ingresadas
    por el usuario. 
    '''
    caracteres = string.ascii_lowercase

    if usar_mayusculas:
        caracteres += string.ascii_uppercase

    if usar_especiales:
        caracteres += string.punctuation
    
    if usar_numeros:
        caracteres += string.digits

    if usar_primos:
        caracteres += obtener_primos(longitud)
        
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

"""
=========funcion de generacion de numeros primos para la contraseña  ===========
"""

def obtener_primos(cantidad):
    '''
    La funcion obtener_primos
    recibe: una cantidad de numeros primos para generar
    devuelve: los numeros primos se devuelven en cadena y se concatenan para 
    formar una sola cadena que se devuelve. 
    '''

    primos = []

    numero = 5 

    paso = 2  
    
    while len(primos) < cantidad:
        '''
        Este condicional comprueba si el numero actual (numero) es primo. 
        Verifica que numero no sea divisible por un numero anterior en la lista 
        primos. 
        '''
        if all(numero % p != 0 for p in primos):

            primos.append(numero)

        '''
        Se incrementa numero por el valor de paso. Esto nos permite avanzar al 
        siguiente numero de la secuencia 6k+1
        '''
        numero += paso
        
        '''
        Cambiamos el valor de paso para alternar  entre 2 (que representa 6k-1) 
        y 4 (que representa 6k+1).
        '''
        paso = 6 - paso
    
    return ''.join(str(p) for p in primos)

def main():
    contraseñas_generadas = []
    try:
        cantidad_ejecuciones = int(
            input("¿Cuántas veces deseas generar contraseñas?: "))

        cantidad_contraseñas = int(
            input("¿Cuántas contraseñas deseas generar?: "))


        longitud = int(input("Ingresa la longitud de las contraseñas: "))

        usar_mayusculas = input(
            "¿Quieres usar letras mayúsculas? (s/n): ").lower() == 's'

        usar_especiales = input(
            "¿Quieres usar caracteres especiales? (s/n): ").lower() == 's'

        usar_numeros = input(
            "¿Quieres usar números? (s/n): ").lower() == 's'

        usar_primos = input(
            "¿Quieres usar números primos? (s/n): ").lower() == 's'
        
        '''
        Este bucle nos permite iterar la generacion de las contraseñas segun la 
        cantidad especificada en cantidad_ejecuciones. 
        '''
        for _ in range(cantidad_ejecuciones):

            contraseñas_generadas_ejecucion = []

            '''
            Este bucle nos permite generar multiples contraseñas en cada 
            ejecucion, que se almacenaran en la lista creada anteriormente. 
            '''
            for _ in range(cantidad_contraseñas):
                contraseña_generada = generar_contraseña(longitud, 
                usar_mayusculas, usar_especiales, 
                usar_numeros, usar_primos)
                
                contraseñas_generadas_ejecucion.append(contraseña_generada)
            
            contraseñas_generadas.append(contraseñas_generadas_ejecucion)


        print("\nContraseñas generadas:")

        for i, ejecucion in enumerate(contraseñas_generadas, start=1):

            print(f"Ejecución {i}:")

            for j, contraseña in enumerate(ejecucion, start=1):

                print(f"{j}. {contraseña}")
    except ValueError:
        print("Por favor, ingresa una longitud o cantidad válida.")

if __name__ == "__main__":
    main()
