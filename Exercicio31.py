n = 1
soma_pares = 0
soma_impares = 0
soma_total = 0

while n != 0:
  n = int(input())
  soma_total += n
  if n % 2 == 0:
    soma_pares += n
  else:
    soma_impares += n
    
print(soma_pares)
print(soma_impares)
print(soma_total)
  
  

  