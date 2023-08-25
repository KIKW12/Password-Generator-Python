# Solicitar al usuario que ingrese el límite superior hasta el cual queremos encontrar números primos.
limite = int(input("Ingrese el límite superior: "))

# Imprimir un mensaje para informar qué se mostrarán los números primos hasta el límite ingresado.
print("Números primos hasta", limite, ":")

# Iterar a través de los números en el rango desde 2 hasta el límite ingresado.
for num in range(2, limite + 1):

    # Inicializar una variable para rastrear si el número actual es primo.
    es_primo = True
    
    # Iterar a través de los números desde 2 hasta la raíz cuadrada de 'num' más 1.
    for i in range(2, int(num ** 0.5) + 1):

        # Verificar si 'num' es divisible por 'i' sin dejar residuo.
        if num % i == 0:
            # Si es divisible, marcar 'es_primo' como False y salir del bucle interno.
            es_primo = False
            break
    
    # Después de completar el bucle interno, verificar si 'es_primo' sigue siendo True.
    if es_primo:
        # Si 'es_primo' es True, imprimir el número 'num' en la misma línea.
        print(num, end=" ")

