def avaliacao_carro(preco):
    if preco < 10000:
        return "malestado"
    elif preco < 30000:
        return "conservado"
    elif preco < 60000:
        return "seminovo"
    else:
        return "novo"


preco_do_carro = float(input("Por favor, digite o preço do carro: "))
avaliacao_preco = avaliacao_carro(preco_do_carro)


print(avaliacao_preco)
