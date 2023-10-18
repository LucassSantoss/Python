def mais_frequente(lista):
    i = 0
    maior_frequencia = lista[0]
    qntd_vezes_maior = 0
    while i < len(lista):
        j = 0
        qntd_vezes = 0
        while j < len(lista):
            if maior_frequencia == lista[j]:
                qntd_vezes_maior += 1
            j += 1
        j = 0
        while j < len(lista):
            if lista[i] == lista[j]:
                qntd_vezes += 1
            j += 1
        i += 1
        if qntd_vezes > maior_frequencia:
            maior_frequencia = qntd_vezes
            maior = lista[maior_frequencia]
    return maior

print(mais_frequente([1, 2, 2, 3, 4]))
