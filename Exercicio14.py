
numero = int(input())

invertido = numero % 10 * 1000
numero = numero // 10
invertido += numero % 10 * 100
numero = numero // 10
invertido += numero % 10 * 10
numero = numero // 10
invertido += numero % 10


print(invertido)
