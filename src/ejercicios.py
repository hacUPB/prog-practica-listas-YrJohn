# Ejercicio 1: Suma de elementos en una lista de listas
def suma_matriz(matriz):
    """
    Recibe una lista de listas y devuelve la suma de todos sus elementos.
    Incluir el código aquí para sumar los elementos de la matriz.
    """
    #[[3,5,7], [4,8,11]]
    suma = 0
    for filas in matriz:
        for dato in filas:
            suma += dato
    return suma


# Ejercicio 2: Encontrar el valor máximo en una matriz
def maximo_matriz(matriz):
    """
    Recibe una lista de listas y devuelve el valor máximo.
    Incluir el código aquí para encontrar el valor máximo en la matriz.
     """
    pass

# Ejercicio 3: Verificar si un número es primo
def es_primo(n):
    """
    Recibe un número y devuelve True si es primo, False en caso contrario.
    Incluir el código aquí para determinar si un número es primo.
    """
    if n < 2
        return false
    
    for i in range (2,n)
        if n % == 0
            return false
        
    return true


# Ejercicio 4: Transponer una matriz
def transponer_matriz(matriz):
    """
    Recibe una lista de listas y devuelve la matriz transpuesta.
    Incluir el código aquí para transponer la matriz.
    """
pass

# Ejercicio 5: Filtrar números pares
def filtrar_pares(lista):
    """
    Recibe una lista de números y devuelve una nueva lista con solo los números pares.
    Incluir el código aquí para filtrar los números pares.
    """ 
    pares=[]
    for numero in lista:
        if numero % 2 == 0

    pares.append(numero)
    return pares
   

# Ejercicio 6: Contar la cantidad de palabras en una frase
def contar_palabras(frase):
    """
    Recibe una frase y devuelve el número de palabras.
    Incluir el código aquí para contar las palabras en la frase.
    """
    pass

# Ejercicio 7: Crear una tabla de multiplicar
def tabla_multiplicar(n):
    """
    Recibe un número y devuelve una lista con su tabla de multiplicar del 1 al 10.
    Incluir el código aquí para generar la tabla de multiplicar.
    """
    tabla=[]
   contador=1
    while contador<=10
        numerotabla= n*contador
        contador+=1
        tabla.append(numerotabla)

    return tabla

# Ejercicio 8: Contar números negativos en una lista
def contar_negativos(lista):
    """
    Recibe una lista de números y devuelve la cantidad de números negativos.
    Incluir el código aquí para contar los números negativos en la lista.
    """
   contador = 0
for numero in lista:
    if numero < 0:
        contador +=1

return contador

# Ejercicio 9: Determinar si una lista está ordenada
def lista_ordenada(lista):
    """
    Recibe una lista de números y devuelve True si está ordenada de menor a mayor.
    Incluir el código aquí para verificar si la lista está ordenada.
    """
     for i in range(len(lista)-1)
        if lista[i] > lista[i +1]
        return false
    
    return true

# Ejercicio 10: Cifrar un texto con el cifrado César
def cifrado_cesar(texto, desplazamiento):
    """
    Recibe un texto y un desplazamiento, y devuelve el texto cifrado usando el cifrado César.
    Incluir el código aquí para cifrar el texto con el cifrado César.
    """
   
    pass


#Aquí comienza el progrma principal. No modifiques el código debajo de esta línea.
def main():
    pass


if __name__ == "__main__":
    main() 
    
    
    
    
    
    
    