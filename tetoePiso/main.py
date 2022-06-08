def pesquisa_binaria_recursiva(A, esquerda, direita, item):

    if item < A[0]:
        return item, A[0], -1

    if item > A[len(A)-1]:
        return item, -1, A[len(A)-1]

    if direita < esquerda:
        return -1

    meio = (esquerda + direita) // 2

    if A[meio] == item:
        return item, item, item

    elif A[meio] > item:
        if A[meio-1] < item:
            return item, A[meio], A[meio-1]

        return pesquisa_binaria_recursiva(A, esquerda, meio - 1, item)
    else:
        if A[meio+1] > item:
            return item, A[meio+1], A[meio]

        return pesquisa_binaria_recursiva(A, meio + 1, direita, item)


A = [1, 4, 6, 8, 9, 11]
X = int(input('Digita ae: '))

k, teto, piso = pesquisa_binaria_recursiva(A, 0, len(A) - 1, X)

print(f'k = {k} --> teto = {teto}, piso = {piso}')
