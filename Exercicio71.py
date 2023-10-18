string_a = input()
string_b = input()
string_a_sem_espaco = []
string_b_sem_espaco = []

def sem_espaco(a, b):
    for i in a:
        if i != ' ':
            b.append(i)

sem_espaco(string_a, string_a_sem_espaco)
sem_espaco(string_b, string_b_sem_espaco)

anagrama = 1
soma_anagrama = 0
i = 0
while i < len(string_a_sem_espaco) and anagrama == 1:
    j = 0
    soma_anagrama = 0
    while j < len(string_b_sem_espaco) and anagrama == 1:
        if string_a_sem_espaco[i] == string_b_sem_espaco[j]:
            soma_anagrama += 1
        j += 1
    if soma_anagrama == 0:
        anagrama = 0
    i += 1

soma_anagrama = 0
i = 0
while i < len(string_b_sem_espaco) and anagrama == 1:
    j = 0
    soma_anagrama = 0
    while j < len(string_a_sem_espaco) and anagrama == 1:
        if string_b_sem_espaco[i] == string_a_sem_espaco[j]:
            soma_anagrama += 1
        j += 1
    if soma_anagrama == 0:
        anagrama = 0
    i += 1

print(anagrama)