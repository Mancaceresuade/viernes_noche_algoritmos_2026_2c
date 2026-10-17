

def main():
    matriz=[[1,2,3],[5,3,1],[8,3,1]]
    print(algunaFilaConTodosParesYDiagonalDescendenteCoincideConAlgunaFila(matriz))

def algunaFilaConTodosParesYDiagonalDescendenteCoincideConAlgunaFila(matriz):
    return algunaFilaConTodosPares(matriz) and diagonalDescendenteCoincideConAlgunaFila(matriz)

def algunaFilaConTodosPares(matriz):
    rta = False
    for fila in matriz:
        rta = rta or filaTodosPares(fila)
    return rta

def filaTodosPares(fila):
    rta = True
    for elemento in fila:
        rta = rta and esPar(elemento)
    return rta

def esPar(elemento):
    return elemento%2==0

def diagonalDescendenteCoincideConAlgunaFila(matriz):
    rta = False
    for fila in matriz:
        rta = rta or diagonalCoincideConFila(matriz,fila)
    return rta
def diagonalCoincideConFila(matriz,fila):
    # precondicion: matriz cuadrada
    rta = True
    for i in range(len(matriz)):
        if(matriz[i][i]!=fila[i]):
            rta = False
    return rta

def ejemplo_lista():
    lista=[4,5,6,7]
    print(len(lista))
    for i in range(0,len(lista),1):
        print(str(i)+" " +str(lista[i]))

    for numero in lista:
        print(numero)    

main()    