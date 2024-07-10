def separar(lista):
    global pares
    global impares 
    pares = []
    impares = []
    for x in lista:
        if x % 2 == 0:
            pares.append(x)
        else:
            impares.append(x)
    return pares,impares

#pares = [] , la otra solucion es dejar las listas de los pares e impares fuera de la funcion, en vez de definirla dentro como "global"
#impares = []
lista = [6,5,2,1,7]
separar(lista)
print("Los numeros pares de la lista son:",pares)
print("Los numeros impares de la lista son:",impares)