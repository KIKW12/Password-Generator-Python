# TC1028 Proyecto Juan Enrique Ayala Zapata

## Generador de Password

### Contexto

"En la actualidad, sabemos que debemos cambiar nuestras contraseñas cada cierto tiempo para evitar que personas indeseadas accesen a nuestras cuentas personales y toda nuestra informacion.
Se sabe que es recomendable cambiar de contraseñas al menos cada 3 meses, pero siempre llegamos a la capacidad límite de nuestro cerebro para poder crear nuevas combinaciones, es por ello
que este programa te permitirá crear una nueva contraseña que cumpla con los parámetros que tu le pidas, ya sea que contenga letras mayúsculas, minúsculas, caracteres especiales, así como 
la longitud deseada."


Este programa es un generador de contraseñas de acuerdo a las características requeridas por el usuario. El programa corre en la terminal de python3. Muestra una serie de elementos que debe 
de llenar el usuario asignando las características de la contraseña requerida. Al final, imprime la contraseña cumpliendo los parámetros ya establecidos. 

### Avance 2
En este avance se implementó un elemento importante para el generador de contraseñas, un generador de numeros primos. Este funciona pidiéndole al usuario un límite superior, para poder
calcular todos los números primos hasta el límite dado por el usuario. En posteriores avances se realizará un cambio en esta parte para que sea de manera más autónoma.

### Avance 3

En este avance se transforma el codigo anteriormente presentando a una funcion, para durante el desarrollo del proyecto, sea más fácil acceder a cada una de las partes del código. Se realizó la optimización del proceso para saber si un numero es primo utilizando un patron llamado "El patrón de los números primos" que se presenta de la forma x = 6k + 1 y x = 6k - 1. 
Un ejemplo de este patrón es x = (6)(1) - 1, siendo x = 5. Como sabemos, 5 es numero primo. 

### Avance 4

Este avance pide la implementación de estrcuturas de decisión, en el código ya se encontraban desde el avance 3, estas estructuras se encuentran dentro de la función "es_primo". Se utilizan para comprar si el numero ingresado o no cumple con algunas condicioes para saber si es primo o no, antes de entrar al proceso de optimización. 
