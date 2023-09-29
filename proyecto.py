'''Random se utiliza para generar aleatoriamente caracteres de la contraseña.'''
import random

'''
String proporciona constantes con caracteres como letras mayusculas y minusculas, 
digitos y caracteres especiales.
'''
import string

'''
La funcion generar_contraseña
recibe: longitud de la constraseña, usar_mayusculas un booleano que indica si el usuario necesita o no 
letras mayusculas, usar_especiales un booleano que indica si se deben usar caracteres especiales, 
usar_numeros un booleano que indica si se deben usar numeros en la contraseña y usar_primos un booleano
que indica si se deben de utilizar numeros primos en la constraseña.
regresa: una contraseña cumpliendo con las especificaciones ingresadas por el usuario. 

'''
def generar_contraseña(longitud, usar_mayusculas, usar_especiales, usar_numeros, usar_primos):
    '''
    Se crea la variable caracteres, que solo contiene letras del alfabeto ASCII en mayusculas y minusculas.
    '''
    caracteres = string.ascii_lowercase
    
    '''
    Si se cumple la condicion de que la contraseña debe de llevar letras mayusculas, a la variable
    caracteres se le agregan letras random del alfabeto ASCII en mayusculas. 
    '''
    if usar_mayusculas:
        caracteres += string.ascii_uppercase

    '''
    Si se cumple la condicion de que la contraseña debe de llevar caracteres especiales, a la variable 
    caracteres se le agregan estos.
    '''
    if usar_especiales:
        caracteres += string.punctuation
    
    '''
    Si se cumple la condicion de que la contraseña debe de llevar numeros, se le agrega a la variable 
    caracteres los digitos del 0 al 9.
    '''
    if usar_numeros:
        caracteres += string.digits
    
    '''
    Si se cumple la condicion, se llama a la funcion obtener_primos para obtener numeros primos y se 
    agregan a la cadena de caracteres disponibles. 
    '''
    if usar_primos:
        caracteres += obtener_primos(longitud)
    
    '''
    Se devuelve la constraseña generada.
    '''
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

'''
La funcion obtener_primos
recibe: una cantidad de numeros primos para generar
devuelve: los numeros primos se devuelven en cadena y se concatenan para formar una sola cadena que se
devuelve. 
'''
def obtener_primos(cantidad):
    '''
    Se inicializa una lista vacia que contendra los numeros primos encontrados.
    '''
    primos = []

    '''
    Se incia la variable numero en 5, ya que los primeros numeros primos en el patron 6k±1 son 5 y 7.
    '''
    numero = 5 

    '''
    La variable paso se inicia en 2, esto determina el cambio entre los numeros 6k-1 y 6k+1 alternadamente,
    se comienza en 2 que representa 6k-1.
    '''
    paso = 2  
    
    '''
    Este bucle while se ejecutara hasta que hayamos encontrado la cantidad de numros primos especificados
    'cantidad'.
    '''
    while len(primos) < cantidad:

        '''
        Este condicional comprueba si el numero actual (numero) es primo. Verifica que numero no sea
        divisible por un numero anterior en la lista primos. 
        '''
        if all(numero % p != 0 for p in primos):
            '''
            Si el numero actual que estamos analizando pasa la prueba de ser primo se agrega a la lista. 
            '''
            primos.append(numero)
        '''
        Se incrementa numero por el valor de paso. Esto nos permite avanzar al siguiente numero de la
        secuencia 6k+1
        '''
        numero += paso
        
        '''
        Cambiamos el valor de paso para alternar  entre 2 (que representa 6k-1) y 4 (que representa 
        6k+1).
        '''
        paso = 6 - paso
    
    '''
    Cuando se alcanza la cantidad deseada de numeros primos, se conviertenen en cadena de texto y se 
    devuelven. 
    '''
    return ''.join(str(p) for p in primos)


def main():
    '''
    Se crea la lista contraseñas_generadas vacia para almacenar las contraseñas generadas. 
    '''
    contraseñas_generadas = []

    try:
        '''
        Se le pide al usuario que especifique cuantas veces decea ejecutar la generacion de las contraseñas
        en una sola ejecucion del programa. Lo que permite generar conuntos separados de contraseñas en
        cada ejecucion. 
        '''
        cantidad_ejecuciones = int(input("¿Cuántas veces deseas generar contraseñas?: "))
        '''
        Se le pide al usuario la cantidad de contraseñas que quiera generar
        '''
        cantidad_contraseñas = int(input("¿Cuántas contraseñas deseas generar?: "))

        '''
        Se le pide al usuario que ingrese la longitud deseada de las contraseñas.
        '''
        longitud = int(input("Ingresa la longitud de las contraseñas: "))

        '''
        Se le pregunta al usuario si desea que sus contraseñas lleven o no letras mayusculas, se convierte
        a minuscula su respuesta para realizar la validación. 
        '''
        usar_mayusculas = input("¿Quieres usar letras mayúsculas? (s/n): ").lower() == 's'

        '''
        Se le pregunta al usuario si desea que las contraseña lleven o no caracteres especiales del alfabeto
        ASCII, se convierte a minuscula la respuesta para realizar la validación. 
        '''
        usar_especiales = input("¿Quieres usar caracteres especiales? (s/n): ").lower() == 's'

        '''
        Se le pregunta al usuario si desea que las contraseñas lleven o no numeros, se convierte a minuscula
        la respuesta para realizar la validación.
        '''
        usar_numeros = input("¿Quieres usar números? (s/n): ").lower() == 's'

        '''
        Se le pregunta al usuario si desea que las contraseñas lleven o no numeros primos, 
        se convierte a minuscula la respuesta para realizar la validación.
        '''
        usar_primos = input("¿Quieres usar números primos? (s/n): ").lower() == 's'
        
        '''
        Este bucle nos permite iterar la generacion de las contraseñas segun la cantidad especificada en 
        cantidad_ejecuciones. 
        '''
        for _ in range(cantidad_ejecuciones):
            '''
            En cada iteracion del bucle, se crea una lista llamada contraseñas_generadas_ejecucion para
            almacenar las contraceñas generadas en una ejecucion especifica. 
            '''
            contraseñas_generadas_ejecucion = []

            '''
            Este bucle nos permite generar multiples contraseñas en cada ejecucion, que se almacenaran en 
            la lista creada anteriormente. 
            '''
            for _ in range(cantidad_contraseñas):
                contraseña_generada = generar_contraseña(longitud, usar_mayusculas, usar_especiales, usar_numeros, usar_primos)
                
                '''
                Despues de generar todas las contraseñas generadas en una ejecución específica, se agrega
                a la lista principal contraseñas_generadas, creando la estructura de lista anidada. 
                '''
                contraseñas_generadas_ejecucion.append(contraseña_generada)
            
            '''
            Despues de generar todas las contraseñas en una ejecucion especifica, la lista donde se 
            almacenan estas, se agrega a la lista principal. 
            '''
            contraseñas_generadas.append(contraseñas_generadas_ejecucion)


        print("\nContraseñas generadas:")

        '''
        El bucle nos permite iterar a traves de las diferentes ejecuciones de la generacion de contraseñas
        almacenadas en la lista princiapl contraseñas_generadas. La funcion enumerate se utiliza para
        obtener el tanto indice de i como la ejecucion actual. 
        '''
        for i, ejecucion in enumerate(contraseñas_generadas, start=1):

            '''
            En cada iteracion de este bucle se imprime una linea que indica en eque ejecucion se encuentra.
            '''
            print(f"Ejecución {i}:")

            '''
            Este bucle se utiliza para iterar a travez de las siguientes contraseñas generadas en la 
            ejecucion actual. Se utiliza enumerate para obtener el indice j como la contraseña actual. 
            '''
            for j, contraseña in enumerate(ejecucion, start=1):

                '''
                En cada iteracion de este bucle se imprime una linea que muestra el indice de la contraseña
                y la contraseña.
                '''
                print(f"{j}. {contraseña}")
    except ValueError:
        print("Por favor, ingresa una longitud o cantidad válida.")

if __name__ == "__main__":
    main()
