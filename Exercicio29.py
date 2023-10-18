x = int(input())
y = int(input())
a = x
b = y

if x <= y:
  while a <= y:
    print(a)
    a = a + 1
  while x <= b:
    print(b)
    b = b - 1
else:
  print("INVALIDO")