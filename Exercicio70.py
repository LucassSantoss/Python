string = input()
palindromo = 1
string_sem_espaco = []
for letra in string:
    if letra != ' ':
        string_sem_espaco.append(letra)

primeiro = 0
ultimo = len(string_sem_espaco) - 1
while primeiro <= len(string_sem_espaco) // 2 and palindromo == 1:
    if string_sem_espaco[primeiro] != string_sem_espaco[ultimo]:
        palindromo = 0 
    primeiro += 1
    ultimo -= 1
print(palindromo)