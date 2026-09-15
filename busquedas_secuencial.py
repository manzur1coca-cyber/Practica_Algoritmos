def buscar_numero (x, v: list, t):
    encontrado= False
    i = 0
    while encontrado != True and i < t:
        if v[i] == x:
            encontrado= True
        else:
            i = i + 1 

    if encontrado == True:
            return i
    else:
            return -1


def iniciar_programa():
    print("Este programa fue realizado para encontrar la posición de un número en un array") 
    v=[12,7,25,4,18,9]
    tamaño= 6
    num =4
    print(v)
    print ("El número que deseo buscar es: ", num)
    pos = buscar_numero(num, v, tamaño)
    print("El número buscado se encuentra en la posición: ", pos)

iniciar_programa()