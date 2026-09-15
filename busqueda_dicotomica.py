def ordenar_vector(v):
    i=0
    j= 0
    aux=0
    for i in range(0,5):

        for j in range((i+1), 6):

            if v[i] > v[j]:
                aux = v[i]
                v[i] = v[j]
                v[j] = aux


def buscar_numero(n, v, x):
    inicio = 0
    final= x
    encontrado = False
    while encontrado != True and inicio < final:
        medio= (inicio + final) // 2
        if v[medio] == n:
            encontrado = True
        elif(v[medio] > n):
            final = medio -1   
        else:
            inicio = medio + 1
                
    if encontrado == True:
        return medio
    else:
        return -1
            
    




def iniciar_programa():
    print("Este programa fue realizado para encontrar la posición de un número en un array") 
    print ("")
    print("Array original")
    v=[12,7,25,4,18,9]
    print(v)
    print ("")
    print("Array ordenado, para poder realizar la busqueda dicotomica")
    ordenar_vector(v)
    tamaño = 5
    num =9
    print(v)
    print ("")
    print ("El número que deseo buscar es: ", num)
    pos = buscar_numero(num, v, tamaño)
    print ("")
    print("El número buscado se encuentra en la posición: ", pos)

iniciar_programa()