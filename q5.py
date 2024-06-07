preco = float(input("Por favor, digite o preço do carro: "))

if preco < 10000:
    print("malestado")
elif preco < 30000:
    print("conservado")
elif preco < 60000:
    print("seminovo")
else:
    print("novo")
