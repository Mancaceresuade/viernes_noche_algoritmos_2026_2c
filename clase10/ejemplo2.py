# Acumuladores booleanos
# Para todos los elementos que pertenecen al conjunto lista
# devolver verdador si son todos pares
# -> variable auxiliar en true
# -> ciclo con y

def main():
    matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 5, 3] ]
    # print(matriz)
    # print(matriz[0][0])
    #imprimirMatriz(matriz)
    #imprimirDiagonalDescendente(matriz)
    #imprimirDiagonalAscendente(matriz)
    # ejercicio tipo parcial
    print(coincidenElementosEnOrdenDiagonalAscendenteConAlgunaFila(matriz))

def coincidenElementosEnOrdenDiagonalAscendenteConAlgunaFila(matriz):
    diagonal=diagonal_ascendente(matriz)
    for fila in matriz:
        if(fila==diagonal):
            return True
    return False

def diagonal_ascendente(matriz):
    lista=[]
    for i in range(len(matriz)):
        lista.append( matriz[len(matriz)-i-1][i])
    return lista    

def imprimirDiagonalAscendente(matriz):
    # prencondicion: matriz si es cuadrada
    for i in range(len(matriz)):
        #print(str(len(matriz)-i)+ " " + str(i))
        print(matriz[len(matriz)-i-1][i])   


def imprimirDiagonalDescendente(matriz):
    # prencondicion: matriz si es cuadrada
    for i in range(len(matriz)):
         print(matriz[i][i])   


def imprimirMatriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(   str(elemento) + " " , end="" )
        print("")
        

def todosPares(lista):
    if( len(lista)==0):
        return False
    aux = True
    for numero in lista:
        aux = aux and numero%2==0
    return aux

def algunosPares(lista):
    aux = False
    for numero in lista:
        aux = aux or numero%2==0
    return aux

    
def test_todos_pares():
    # camino feliz: todos pares deberia verdadero
    mi_lista=[4,6,8,10]
    print(todosPares(mi_lista))
    # caminos alternativo: todos pares menos el ultimo deberia dar falso
    mi_lista=[4,6,8,9]
    print(todosPares(mi_lista))
    # caminos alternativo: todos pares menos un valor valor del medio deberia dar falso
    mi_lista=[4,6,8,9,10,12]
    print(todosPares(mi_lista))
    # caminos alternativo: todos pares menos el primero deberia dar falso
    mi_lista=[1,4,6,8,90,10,12]
    print(todosPares(mi_lista))
    # caminos alternativo: lista vacia deberia dar falso
    mi_lista=[]
    print(todosPares(mi_lista))

def test_algunosPares():    
    # camino feliz: alguno par deberia devolver true
    mi_lista=[4,6,8,10]
    print(algunosPares(mi_lista))
    # camino alternativo, todos impares da false
    mi_lista=[1,3,5,7]
    print(algunosPares(mi_lista))


main()

