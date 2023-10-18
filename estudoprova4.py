qntd_alunos = int(input("Infore a quantidade de alunos: "))
i = 0
media_turma = 0
mediasomada = 0

while i < qntd_alunos:
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    qntd_provas = int(input("Informe a quantidade de provas: "))
    j = 0
    media_aluno = 0
    while j < qntd_provas:
        notas = float(input(f"Digite a nota {j + 1} do aluno {nome}: "))
        media_aluno += notas
        media_turma += notas
        j += 1
    media_aluno = media_aluno / qntd_provas
    print(f"A média do {nome} é: {media_aluno:.2f}")
    mediasomada += media_aluno
    i += 1

media_turma = mediasomada / qntd_alunos
print(f"A média da turma é: {media_turma:.2f}")

