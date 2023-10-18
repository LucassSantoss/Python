#EXERCICIO 1
def buscar_v1(lista, numero):
    i = 0
    encontrou = -1
    saida = False
    while i < len(lista) and not saida:
        if lista[i] == numero:
            encontrou = i
            saida = True
        i += 1
    return encontrou

def buscar_v2(lista, numero):
    encontrou = -1
    for i in range (len(lista)):
        if lista[i] == numero:
            encontrou = i
            break
    return encontrou

#EXERCICIO 2
def remover_lista(lista, indice):
    i = indice
    removeu = True
    if indice >= 0 and indice < len(lista):
        while i < len(lista) - 1:
            lista[i] = lista[i + 1]
            i += 1
        lista.pop()
        print(lista)
    else:
        removeu = False
    return removeu

#EXERCICIO 3
def inserir_lista(lista, indice, elemento):
    lista.append(0)
    i = len(lista) - 1
    inseriu = True
    if indice >= 0 and indice < len(lista):
        while i >= indice:
            lista[i] = lista[i - 1]
            i -= 1
        lista[indice] = elemento
        print(lista)
    else:
        inseriu = False
    return inseriu

#EXERCICIO 4
def cria_lista():
    lista_criada = []
    return lista_criada

#EXERCICIO 5
def matriz_nula(n, m):
    matriz = []
    for linha in range (n):
        linha = []
        for coluna in range (m):
            linha.append(0)
        matriz.append(linha)
    return matriz

#EXERCICIO 6
def matriz_identidade(n):
    matriz = []
    for linha in range (n):
        linha = []
        for coluna in range (n):
            linha.append(0)
        matriz.append(linha)
    for i in range (len(matriz[1])):
        matriz[i][i] = 1
    return matriz

#EXERCICIO 7
def listas_iguais(lista1, lista2):
    if len(lista1) == len(lista2):
        i = 0
        while i < len(lista1):
            if lista1[i] != lista2[i]:
                return False
            i += 1
        return True
    return False

#EXERCICIO 8
def quantidade_elementos_iguais(lista1, lista2):
    if len(lista1) == len(lista2):
        i = 0
        while i < len(lista1):
            quantidade_vezes = 0
            j = 0
            while j < len(lista1):
                if lista1[i] == lista1[j]:
                    quantidade_vezes += 1
                j += 1
            quantidade_vezes_2 = 0
            j = 0
            while j < len(lista2):
                if lista1[i] == lista2[j]:
                    quantidade_vezes_2 += 1
                j += 1
            if quantidade_vezes != quantidade_vezes_2:
                return False
            i += 1
        return True
    else:
        return False

#EXERCICIO 9
def ordem_crescente(lista):
    for i in range (len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

#EXECICIO 10
def string_caracteres_diferentes(string):
    i = 0
    quantidade_vezes = 0
    while i < len(string):
        j = 0
        quantidade_vezes = 0
        while j < len(string):
            if string[i] == string[j]:
                quantidade_vezes += 1
            j += 1
        if quantidade_vezes > 1:
            return False
        i += 1
    return True

#EXERCICIO 11
def esta_contido(string1, string2):
    i = 0
    while i < len(string2):
        j = 0
        quantidade_vezes = 0
        while j < len(string1):
            if string2[i] == string1[j]:
                quantidade_vezes += 1
            j += 1
        if quantidade_vezes == 0:
            return False
        i += 1
    return True

#EXERCICIO 12
def sem_repeticao(lista):
    lista_sem_repeticao = []
    lista_sem_repeticao.append(lista[0])
    i = 0
    while i < len(lista):
        j = 0
        quantidade_vezes = 0
        while j < len(lista_sem_repeticao):
            if lista[i] == lista_sem_repeticao[j]:
                quantidade_vezes += 1
            j += 1
        if quantidade_vezes == 0:
            lista_sem_repeticao.append(lista[i])
        i += 1
    return lista_sem_repeticao

#EXERCICIO 13
def interseccao_listas(lista1, lista2):
    lista_interseccao = []
    i = 0
    while i < len(lista1):
        j = 0
        while j < len(lista2):
            if lista1[i] == lista2[j]:
                lista_interseccao.append(lista1[i])
                break
            j += 1
        i += 1
    return lista_interseccao

#EXERCICIO 14
def palindromo(string):
    j = len(string) - 1
    for i in range (len(string) // 2):
        if string[i] != string[j]:
            return False
        j -= 1
    return True

#EXERCICIO 15
def procurar_sequencia_fibonacci(numero):
    fibonacci = [1, 1]
    aux_numero = numero
    if numero < 5:
        aux_numero += 1
    i = 1
    while i <= aux_numero:
        fibonacci.append(fibonacci[i] + fibonacci[i - 1])
        i += 1
    for elemento in fibonacci:
        if elemento == numero:
            return True
    return False

#EXERCICIO 16
def strings_iguais(string1, string2):
    if len(string1) == len(string2):
        j = 0
        for elemento in string1:
            if elemento != string2[j]:
                return False
            j += 1
        return True
    return False

#EXERCICIO 17
def lista_numeros_primos(lista):
    i = 0
    while i < len(lista):
        soma_divisores = 0
        divisor = 1
        while divisor <= lista[i] // 2:
            if lista[i] % divisor == 0:
                soma_divisores += 1
            divisor += 1
        if soma_divisores != 1:
            return False
        i += 1
    return True

#EXERCICIO 18
def matriz_quadrado_magico(matriz_quadrada):
    if len(matriz_quadrada) == len(matriz_quadrada[0]):
        i = 0
        j = 0
        soma_diagonal_principal = 0
        while i < len(matriz_quadrada):
            soma_diagonal_principal += matriz_quadrada[i][j]
            i += 1
            j += 1
        i = 0
        while i < len(matriz_quadrada):
            j = 0
            soma_linha = 0
            while j < len(matriz_quadrada):
                soma_linha += matriz_quadrada[i][j]
                j += 1
            if soma_linha != soma_diagonal_principal:
                return False
            i += 1
        j = 0
        while j < len(matriz_quadrada):
            i = 0
            soma_coluna = 0
            while i < len(matriz_quadrada):
                soma_coluna += matriz_quadrada[i][j]
                i += 1
            if soma_coluna != soma_diagonal_principal and soma_diagonal_principal != soma_linha:
                return False
            j += 1
        return True
    return False

#EXERCICIO 19
def media_sem_repeticao(lista):
    lista_sem_repeticao = [lista[0]]
    i = 1
    while i < len(lista):
        j = 0
        quantidade_vezes = 0
        while j < len(lista_sem_repeticao):
            if lista[i] == lista_sem_repeticao[j]:
                quantidade_vezes += 1
            j += 1
        if quantidade_vezes == 0:
            lista_sem_repeticao.append(lista[i])
        i += 1
    print(f"Sua lista sem repetição é {lista_sem_repeticao}")
    media = 0
    for elemento in lista_sem_repeticao:
        media += elemento
    media = media / len(lista_sem_repeticao)
    return media

#EXERCICIO 20
def soma_matriz(matriz1, matriz2):
    i = 0
    matriz3 = []
    while i < len(matriz1):
        j = 0
        linha_matriz3 = []
        while j < len(matriz1[0]):
            linha_matriz3.append(matriz1[i][j] + matriz2[i][j])
            j += 1
        matriz3.append(linha_matriz3)
        i += 1
    return matriz3

def matriz_transposta(matriz):
    matriz_transposta = []
    for i in range (len(matriz[0])):
        linha = []
        for j in range (len(matriz)):
            linha.append(matriz[j][i])
        matriz_transposta.append(linha)
    return matriz_transposta

#------------------TESTES------------------#

lista = [1, 2, 3, 4, 5, 6, 7]

#print(f"Seu número indicado foi achado na posição {buscar_v2(lista, 3)} (começando pelo 0)")

#print(remover_lista(lista, 3))

#print(inserir_lista(lista, 2, 500))

#print(cria_lista())

#print(matriz_nula(3, 3))

#print(matriz_identidade[3])

#print(listas_iguais(lista, [1, 2, 3, 4, 5, 6, 7]))

#print(quantidade_elementos_iguais([1, 1, 1, 2, 2], [1, 2, 1, 2, 1]))

#print(ordem_crescente([1, 2, 3, 4, 5, 6]))

#print(string_caracteres_diferentes("suco"))
#print(string_caracteres_diferentes("amora"))
#print(string_caracteres_diferentes("sabor"))

#print(esta_contido("camarao", "amor"))
#print(esta_contido("sabor", "amora"))

#print(sem_repeticao("amora"))
#print(sem_repeticao([1, 2, 3, 1, 4, 2, 5]))

#print(interseccao_listas("banana", "amor"))
#print(interseccao_listas("amor", "sabio"))
#print(interseccao_listas([1, 2, 3, 4, 5], [2, 1, 3, 1, 5, 6, 7]))

#print(palindromo("amor a roma"))

#print(procurar_sequencia_fibonacci(8))

#print(strings_iguais("sabor", "amora"))

#print(lista_numeros_primos([2, 3, 5, 7, 11, 3, 13, 17]))

#print(matriz_quadrado_magico([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))

#print(media_sem_repeticao([1, 2, 3, 3, 3, 3, 3, 4, 5, 6]))

#print(soma_matriz([[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]))

print(matriz_transposta([[1, 2, 3], [4, 5, 6]]))