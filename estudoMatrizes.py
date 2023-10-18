def palindromo(string):
    resultado = 1
    i = 0
    j = len(string) - 1
    while i < len(string) // 2:
        if string[i] == ' ':
            i += 1
        if string[j] == ' ':
            j -= 1
        if string[i] != string[j]:
            resultado = 0
            break
        i += 1
        j -= 1
    print(resultado)

#palindromo("ze de lima rua laura mil e dez")

def anagrama(string1, string2):
    string1_sem_espaco = []
    string2_sem_espaco = []
    resultado = 0
    for elem in string1:
        if elem != ' ':
            string1_sem_espaco.append(elem)
    for elem in string2:
        if elem != ' ':
            string2_sem_espaco.append(elem)
    i = 0
    while i < len(string1_sem_espaco):
        j = 0
        quantidade_vezes1 = 0
        while j < len(string1_sem_espaco):
            if string1_sem_espaco[i] == string1_sem_espaco[j]:
                quantidade_vezes1 += 1
            j += 1
        j = 0
        quantidade_vezes2 = 0
        while j < len(string2_sem_espaco):
            if string1_sem_espaco[i] == string2_sem_espaco[j]:
                quantidade_vezes2 += 1
            j += 1
        if quantidade_vezes1 != quantidade_vezes2:
            return 0
        i += 1
    return 1

#print(anagrama('algoritmo', 'logaritmo'))

def imprime_matriz(dimensao, lista):
    matriz = []
    elemento = 0
    for i in range (dimensao[0]):
        linha = []
        for j in range (dimensao[1]):
            linha.append(lista[elemento])
            elemento += 1
        matriz.append(linha)
    i = 0
    for linha in matriz:
        for elem in linha:
            print(elem, end=' ')
        print()


#imprime_matriz([3, 3], [1, 2, 3, 4, 5, 6, 7, 8, 9])

def soma_linha_matriz(dimensao, lista):
    matriz = []
    elemento = 0
    for i in range (dimensao[0]):
        linha = []
        for j in range(dimensao[1]):
            linha.append(lista[elemento])
            elemento += 1
        matriz.append(linha)
    i = 0
    while i < len(matriz):
        j = 0
        soma_linha = 0
        while j < len(matriz[i]):
            soma_linha += matriz[i][j]
            j += 1
        print(f"Soma da linha {i} é: {soma_linha} !")
        i += 1

#soma_linha_matriz([3, 3], [1, 2, 3, 4, 5, 6, 7, 8, 9])

def soma_coluna_matriz(dimensao, lista):
    matriz = []
    elemento = 0
    for i in range (dimensao[0]):
        linha = []
        for j in range (dimensao[1]):
            linha.append(lista[elemento])
            elemento += 1
        matriz.append(linha)
    j = 0
    while j < len(matriz[0]):
        soma_coluna = 0
        i = 0
        while i < len(matriz):
            soma_coluna += matriz[i][j]
            i += 1
        print(f"Soma da coluna {j} é: {soma_coluna} !")
        j += 1

#soma_coluna_matriz([3, 3], [1, 2, 3, 4, 5, 6, 7, 8, 9])

def matriz_transposta(matriz):
    matriz_transposta = []
    for i in range (len(matriz)):
        linha = []
        for j in range (len(matriz[i])):
            linha.append(matriz[j][i])
        matriz_transposta.append(linha)
    print(matriz_transposta)

#matriz_transposta([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def buscar(lista, numero):
    for elem in lista:
        if numero == elem:
            return True
    return False

#print(buscar([1, 2, 3, 4, 5], 8))