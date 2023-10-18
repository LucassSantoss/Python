ano = int(input())

if ano <= 0:
    print("-1")
elif ano % 400 == 0:
    print("1")
elif ano % 4 == 0 and ano % 100 != 0:
    print("1")
else:
    print("0")