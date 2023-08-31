
'''
Avance 3 Proyecto Generador de Contraeñas
'''
def es_primo(numero):
    '''
    La funcion es_primo
    recibe: un numero aleatorio
    devuelve True si el numero es primo y False en caso contrario.
    '''
    if numero <= 1:
        return False
    '''
    Si numero es menor o igual que 1, no se cumple la condicion de que sea un numero primo, entonces se 
    devuelve false.
    '''

    if numero <= 3:
        return True
    '''
    Si numero es 2 o 3, se cumple la condicion de que es un numero primo, entonce se devuelve true.
    '''

    if numero % 2 == 0 or numero % 3 == 0:
        return False
    '''
    Si el numero es divisible entre 2 o 3, y no es ni 2 ni 3, no se cumple la condicion de que sea un un
    numero primo, por lo que se devuelve false. 
    '''

    '''
    La función usa un enfoque optimizado para verificar si numero es divisible por algún número primo más 
    grande que 3. Utiliza un bucle while con i inicializado en 5. Comienza verificando si numero es 
    divisible por i o i + 2.
    '''
    i = 5

    '''
    El bucle while se ejecutara mientras el cuadrado de i sea menor o igual al numero que estamos
    evaluando. 
    '''
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        '''
        En cada iteracion del bucle, se verifica si numero es divisible entre i o i+2. Si numero es 
        divisible por alguno de estos valores sabemos que no es un numero primo y se devuelve false. 
        '''
        i += 6
    '''
    Se incrementa i en 6, aprovechando el patron de los numeros primos 6k±1. Cada iteracion nos mueve a 
    los siguientes candidatos para ser evaluados. 
    '''
    return True
    '''
    Si durante el bucle no se encontro ningun divisor de numero, esto significa que es primo y retornamos
    True. 
    '''



'''
La funcion imrpimir_primos
recibe: paramtero limite, numero mas alto hasta el cual queremos imprimir los numeros primos.
devuelve: el numero que cumple con la condicion de ser primo en la misma linea. 
'''
def imprimir_primos(limite):

    '''
    Este bucle itera de los numeros desde 2 hasta limite + 1. Se inicia el rango en 2 porque es el primo
    mas pequeno posible.
    '''
    for num in range(2, limite + 1):
        if es_primo(num):
            print(num, end=" ")


'''
Se locitia al usuario que ingrese un limite superior, luego se llama a la funcion imprimir_primos de
acuerdo al limite. 
'''
limite_superior = int(input("Ingrese el límite superior: "))
imprimir_primos(limite_superior)
