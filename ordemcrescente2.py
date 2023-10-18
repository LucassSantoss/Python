a = int(input("Informe um numero inteiro: "))
b = int(input("Informe um numero inteiro: "))

if a > b:
  aux = a
  a = b
  b = aux

print(a)  
print(b)
