def binarySearch(item, lista):
    baixo = 0
    alto = len(lista)-1

    while baixo<=alto:
        meio = (baixo+alto)//2
        chute = lista[meio]

    if chute == item:
        return chute
    elif chute < item:
        alto = meio+1
    elif chute > item:
        alto = meio-1
        
    return None


minha_lista = [1,2,3,4,5]
binarySearch(1, minha_lista)#0
binarySearch(-5, minha_lista)#None
